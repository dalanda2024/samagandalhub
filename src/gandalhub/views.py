import os
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .chatbot_data import get_response, suggest_formation

# Charger les variables d'environnement depuis .env.local
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env.local'))

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")
        
        # Utilise notre système de simulation au lieu de Gemini/OpenAI
        response_data = get_response(user_message)
        
        # Format la réponse avec suggestions
        answer = {
            "text": response_data["reponse"],
            "suggestions": response_data["suggestions"]
        }
        
        return JsonResponse({
            "response": answer["text"],
            "suggestions": answer["suggestions"]
        })

    return JsonResponse({"response": "Méthode non autorisée."}, status=405)
