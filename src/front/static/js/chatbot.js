// Ouvre/ferme la fenêtre
document.getElementById('chatbot-trigger').addEventListener('click', function() {
    document.getElementById('chatbot-window').classList.toggle('d-none');
  });
  
  document.getElementById('chatbot-close').addEventListener('click', function() {
    document.getElementById('chatbot-window').classList.add('d-none');
  });
  
  // Envoi de message avec la touche "Entrée" ou le bouton
  document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') sendMessage();
  });
  
  document.getElementById('send-message').addEventListener('click', sendMessage);
  
  function sendMessage() {
  const input = document.getElementById('user-input');
  const message = input.value.trim();

  if (message) {
    const messagesDiv = document.getElementById('chatbot-messages');
    
    // Message utilisateur avec style amélioré
    messagesDiv.innerHTML += `
      <div class="d-flex justify-content-end mb-3">
        <div class="user-message p-3 rounded-lg" style="max-width: 80%; background: #28a745; color: white;">
          ${message}
        </div>
      </div>
    `;

    input.value = '';
    messagesDiv.scrollTop = messagesDiv.scrollHeight;

    // Loader plus informatif
    messagesDiv.innerHTML += `
      <div class="d-flex justify-content-start mb-3" id="ia-loader">
        <div class="ia-message p-3 rounded-lg" style="max-width: 80%;">
          <div class="d-flex align-items-center">
            <span class="spinner-grow spinner-grow-sm text-success me-2"></span>
            <span>Je réfléchis à la meilleure façon de vous aider...</span>
          </div>
        </div>
      </div>
    `;
    messagesDiv.scrollTop = messagesDiv.scrollHeight;

    // Appel à l'API backend Django
    fetch('/api/chat/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
      },
      body: JSON.stringify({ message })
    })
    .then(response => response.json())
    .then(data => {
      const loader = document.getElementById('ia-loader');
      if (loader) loader.remove();

      // Réponse IA avec mise en forme améliorée
      messagesDiv.innerHTML += `
        <div class="d-flex justify-content-start mb-3">
          <div class="ia-message p-3 rounded-lg" style="max-width: 80%; background: #f8f9fa;">
            <div class="mb-2 d-flex align-items-center">
              <i class="fas fa-robot text-success me-2"></i>
              <strong>Assistant GandalHub</strong>
            </div>
            <div style="white-space: pre-line;">
              ${formatResponse(data.response)}
            </div>
          </div>
        </div>
      `;
      messagesDiv.scrollTop = messagesDiv.scrollHeight;
    })
    .catch(() => {
      const loader = document.getElementById('ia-loader');
      if (loader) loader.remove();
      messagesDiv.innerHTML += `
        <div class="d-flex justify-content-start mb-2">
          <div class="ia-message p-2 rounded bg-danger text-white" style="max-width: 80%;">
            Erreur lors de la connexion à l'IA.
          </div>
        </div>
      `;
      messagesDiv.scrollTop = messagesDiv.scrollHeight;
    });
  }
}

// Utilitaire pour récupérer le CSRF token Django
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Formater la réponse avec mise en forme
function formatResponse(text) {
  return text
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/```(\w+)?\n([\s\S]*?)```/g, '<pre><code class="language-$1">$2</code></pre>')
    .replace(/`(.*?)`/g, '<code>$1</code>')
    .replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank">$1</a>');
}