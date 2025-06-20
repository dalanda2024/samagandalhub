FORMATIONS = {
    "techniques": {
        "web": {
            "titre": "Développement Web",
            "duree": "4 mois",
            "prix": "500 000 GNF/mois",
            "lieu": "Campus GandalHub - Kaloum, Conakry",
            "details": "HTML, CSS, JavaScript, React, Node.js"
        },
        "mobile": {
            "titre": "Développement Mobile",
            "duree": "4 mois",
            "prix": "600 000 GNF/mois",
            "lieu": "Campus GandalHub - Kaloum, Conakry",
            "details": "Flutter, React Native, Android Studio"
        },
        "bureautique": {
            "titre": "Bureautique (Word, Excel, PowerPoint)",
            "duree": "2 mois",
            "prix": "200 000 GNF/mois",
            "lieu": "Campus GandalHub - Kaloum, Conakry",
            "details": "Word, Excel, PowerPoint, Internet, Email"
        },
        "reseaux": {
            "titre": "Réseaux Informatiques",
            "duree": "3 mois",
            "prix": "400 000 GNF/mois",
            "lieu": "Campus GandalHub - Kaloum, Conakry",
            "details": "Bases réseaux, Cisco, Sécurité"
        }
    },
    "artisanales": {
        "coiffure": {
            "titre": "Formation Professionnelle en Coiffure",
            "duree": "6 mois",
            "prix": "300 000 GNF/mois",
            "lieu": "Centre Artisanal GandalHub - Matam",
            "partenaire": "Association Guinéenne des Coiffeurs Professionnels"
        },
        "couture": {
            "titre": "Formation en Couture et Design",
            "duree": "6 mois",
            "prix": "300 000 GNF/mois",
            "lieu": "Centre Artisanal GandalHub - Matam",
            "partenaire": "Association des Couturiers de Guinée"
        },
        "patisserie": {
            "titre": "Formation en Pâtisserie",
            "duree": "4 mois",
            "prix": "400 000 GNF/mois",
            "lieu": "Centre Culinaire GandalHub - Matam",
            "partenaire": "École Hôtelière de Conakry"
        },
        "menuiserie": {
            "titre": "Menuiserie & Ebénisterie",
            "duree": "5 mois",
            "prix": "350 000 GNF/mois",
            "lieu": "Centre Artisanal GandalHub - Matam",
            "partenaire": "Association des Artisans de Guinée"
        }
    },
    "langues": {
        "anglais": {
            "titre": "Anglais Général",
            "duree": "3 mois",
            "prix": "250 000 GNF/mois",
            "lieu": "Campus GandalHub - Kaloum, Conakry",
            "details": "Débutant à avancé, conversation, TOEFL"
        },
        "francais": {
            "titre": "Français professionnel",
            "duree": "2 mois",
            "prix": "200 000 GNF/mois",
            "lieu": "Campus GandalHub - Kaloum, Conakry",
            "details": "Expression écrite et orale, rédaction"
        }
    }
}

# Génération automatique des réponses pour chaque formation
def formation_response(formation):
    return f"""🌟 {formation['titre']}

📚 Programme : {formation.get('details', 'Programme détaillé sur demande')}
⏰ Durée : {formation['duree']}
💰 Prix : {formation['prix']}
📍 Lieu : {formation['lieu']}
{f"🤝 En partenariat avec : {formation['partenaire']}" if 'partenaire' in formation else ''}

👉 Voulez-vous voir le programme détaillé ou vous inscrire ?"""

RESPONSES = {
    "salutation": {
        "reponse": """👋 Bonjour ! Je suis l'assistant virtuel de GandalHub.

Je peux vous aider à :
1. Découvrir toutes nos formations (web, bureautique, artisanat, langues...)
2. Vous inscrire ou avoir les tarifs
3. Répondre à vos questions techniques ou vous motiver

Que puis-je faire pour vous aujourd'hui ?""",
        "suggestions": ["Voir les formations", "S'inscrire", "Tarifs"]
    },
    "default": {
        "reponse": """Je n'ai pas bien compris votre demande. Essayez par exemple :
- "Liste des formations"
- "Je veux apprendre la couture"
- "Explique-moi la boucle for"
- "Comment progresser ?"

N'hésitez pas à reformuler ou à demander conseil !""",
        "suggestions": ["Voir les formations", "Tarifs", "Contact"]
    },
    "encouragement": {
        "reponse": """👏 Bravo pour vos efforts ! Continuez ainsi, chaque étape vous rapproche de votre objectif. Besoin d'un conseil ou d'une pause motivation ?""",
        "suggestions": ["Continuer", "Voir mon parcours", "Conseil motivation"]
    },
    "proposition_suivi": {
        "reponse": """🎯 Vous avez terminé un module ! Voulez-vous passer au suivant ou réviser ?
- Continuer vers le prochain module
- Revoir les notions importantes
- Voir votre progression""",
        "suggestions": ["Continuer", "Réviser", "Voir mon parcours"]
    }
}

# Ajout dynamique de chaque formation dans RESPONSES
for domaine, formations in FORMATIONS.items():
    for key, formation in formations.items():
        RESPONSES[f"formation_{key}"] = {
            "reponse": formation_response(formation),
            "suggestions": ["Programme détaillé", "S'inscrire", "Tarifs"]
        }

RESPONSES.update({
    "boucle_js": {
        "reponse": """Une boucle permet de répéter une action plusieurs fois. En JavaScript, la boucle la plus courante est la boucle for :

```javascript
for(let i = 0; i < 5; i++) {
  console.log(i);
}
```
Ce code affiche les nombres de 0 à 4 dans la console.

👉 Si tu veux t'entraîner, commence par notre module "Débuter avec JavaScript". Besoin d'un lien ?""",
        "suggestions": ["Voir le module JavaScript", "Exemples de boucles", "Cours sur les bases JS"]
    },
    "apprendre_patisserie": {
        "reponse": """Parfait ! Je te recommande de commencer par le module ‘Pâtisserie de base’. Tu y apprendras les recettes simples comme les gâteaux au yaourt, les biscuits, etc.

👉 Veux-tu que je t’y emmène ?""",
        "suggestions": ["Voir le module Pâtisserie de base", "Recettes faciles", "S'inscrire"]
    },
    "suivi_html": {
        "reponse": """🎉 Félicitations pour avoir fini le module HTML !
Tu veux passer au module CSS maintenant ou réviser ?

👉 Clique sur “Continuer vers CSS” pour progresser, ou “Réviser HTML” pour consolider tes acquis.""",
        "suggestions": ["Continuer vers CSS", "Réviser HTML", "Voir mon parcours"]
    },
    "decouvrir_formations": {
        "reponse": """Voici toutes nos formations GandalHub :

- Développement Web
- Développement Mobile
- Bureautique (Word, Excel, PowerPoint)
- Réseaux Informatiques
- Coiffure professionnelle
- Couture et design
- Pâtisserie
- Menuiserie & Ebénisterie
- Anglais général
- Français professionnel

Pour chaque formation, je peux vous donner le programme, le prix, la durée ou vous aider à vous inscrire. Laquelle vous intéresse ?""",
        "suggestions": ["Web", "Mobile", "Bureautique", "Réseaux", "Coiffure", "Couture", "Pâtisserie", "Menuiserie", "Anglais", "Français"]
    }
})

FAQ_SIMULATION = {
    "bonjour": {
        "reponse": "👋 Bonjour et bienvenue sur GandalHub, la plateforme qui vous forme aux métiers du numérique et de l’artisanat. Comment puis-je vous aider aujourd'hui ?",
        "suggestions": ["Voir les formations", "S'inscrire", "Contacter un conseiller"]
    },
    "quelles formations proposez-vous": {
        "reponse": """📚 GandalHub propose deux types de formations :

🎓 Formations techniques :
- Développement Web (HTML, CSS, JS, React, Node.js)
- Développement Mobile (Flutter, React Native)

🎨 Formations artisanales :
- Coiffure professionnelle
- Couture & Design
- Pâtisserie

Laquelle vous intéresse ?""",
        "suggestions": ["Développement Web", "Pâtisserie", "Coiffure"]
    },
    "formation en développement web": {
        "reponse": """💻 Formation Développement Web :

- Durée : 4 mois
- Prix : 500 000 GNF/mois
- Lieu : Campus GandalHub - Kaloum, Conakry
- Contenu : HTML5, CSS3, JavaScript, React, Node.js
- Bonus : Projets pratiques, stage, certification

Souhaitez-vous recevoir le programme complet ?""",
        "suggestions": ["Voir programme", "S'inscrire", "Voir autres formations"]
    },
    "formation en pâtisserie": {
        "reponse": """🍰 Formation en Pâtisserie :

- Durée : 4 mois
- Prix : 400 000 GNF/mois
- Lieu : Centre Culinaire GandalHub - Matam
- Contenu : Techniques de base, gâteaux, biscuits, décoration
- Partenaire : École Hôtelière de Conakry

Souhaitez-vous vous inscrire ou recevoir plus d’infos ?""",
        "suggestions": ["S'inscrire", "Voir les tarifs", "Contacter un conseiller"]
    },
    "comment s'inscrire": {
        "reponse": """📝 Procédure d’inscription :

1️⃣ Documents nécessaires :
- Pièce d’identité
- Dernier diplôme
- 2 photos

2️⃣ Frais :
- Frais dossier : 50 000 GNF
- 1er mois de formation à payer

3️⃣ Où ?
- Campus Kaloum ou Centre Matam
- Ou en ligne via notre site officiel

Souhaitez-vous démarrer l’inscription maintenant ?""",
        "suggestions": ["Inscription en ligne", "Prendre RDV", "Voir les formations"]
    },
    "combien coûte la formation web": {
        "reponse": "💰 Le prix de la formation en Développement Web est de 500 000 GNF par mois pendant 4 mois. Frais de dossier : 50 000 GNF.",
        "suggestions": ["Voir contenu", "S'inscrire", "Autres formations"]
    },
    "je veux parler à un conseiller": {
        "reponse": "📞 Vous pouvez contacter un conseiller GandalHub au 625 12 34 56 ou par mail : contact@gandalhub.org. Nous sommes disponibles du lundi au samedi de 9h à 17h.",
        "suggestions": ["Envoyer un message", "Prendre rendez-vous", "Voir les formations"]
    },
    "explique-moi la boucle for en javascript": {
        "reponse": """🔁 La boucle for permet de répéter une action plusieurs fois.

Exemple :
```javascript
for(let i = 0; i < 5; i++) {
  console.log(i);
}
```
Ce code affiche les nombres de 0 à 4.

Veux-tu d'autres exemples ou une explication sur les boucles while ?""",
        "suggestions": ["Exemple boucle while", "Cours JavaScript", "Voir formations web"]
    },
    "exemple de boucle while": {
        "reponse": """🔁 La boucle while permet de répéter une action tant qu'une condition est vraie.

Exemple :
```javascript
let i = 0;
while(i < 5) {
  console.log(i);
  i++;
}
```
Ce code affiche aussi les nombres de 0 à 4.

Tu veux voir la différence entre for et while ?""",
        "suggestions": ["Différence for/while", "Cours JavaScript", "Voir formations web"]
    },
    "comment réviser efficacement": {
        "reponse": "Pour bien réviser : relis tes notes, pratique avec des exercices, pose tes questions au chatbot ou à ton formateur, et participe aux groupes d'entraide.",
        "suggestions": ["Voir supports", "Conseil motivation", "Rejoindre un groupe"]
    },
    "comment réussir ma formation": {
        "reponse": "Pour réussir : sois régulier, pratique chaque jour, demande de l'aide dès que tu bloques, et n'hésite pas à participer aux ateliers et discussions.",
        "suggestions": ["Conseil motivation", "Voir ateliers", "Contact"]
    },
    "comment obtenir une bourse": {
        "reponse": "Nous offrons des bourses aux meilleurs apprenants et selon critères sociaux. Fais une demande auprès de l'administration ou via le formulaire en ligne.",
        "suggestions": ["Demander une bourse", "Voir critères", "Contact"]
    },
    "comment changer de formation": {
        "reponse": "Tu peux changer de formation en début de session ou après discussion avec un conseiller pédagogique. Contacte-nous pour t'accompagner.",
        "suggestions": ["Parler à un conseiller", "Voir formations", "Contact"]
    },
    "comment accéder à mon espace personnel": {
        "reponse": "Après inscription, tu reçois un identifiant et un mot de passe pour accéder à ton espace personnel sur la plateforme GandalHub.",
        "suggestions": ["Aide connexion", "S'inscrire", "Contact"]
    },
    "comment obtenir mon relevé de notes": {
        "reponse": "Ton relevé de notes est disponible dans ton espace personnel ou sur demande à l'administration.",
        "suggestions": ["Voir mon relevé", "Contact", "Voir formations"]
    },
    "comment contacter un formateur": {
        "reponse": "Tu peux contacter ton formateur via la plateforme, par mail ou lors des séances en présentiel. Les coordonnées sont dans ton espace personnel.",
        "suggestions": ["Voir coordonnées", "Contact", "Voir formations"]
    },
    "comment obtenir un emploi après la formation": {
        "reponse": "Nous accompagnons chaque apprenant dans sa recherche d'emploi ou de stage grâce à notre réseau de partenaires et à des ateliers d'insertion.",
        "suggestions": ["Voir partenaires", "Demander un stage", "Conseil emploi"]
    },
    "comment demander un justificatif d'inscription": {
        "reponse": "Un justificatif d'inscription peut être téléchargé depuis ton espace personnel ou demandé à l'accueil du centre.",
        "suggestions": ["Télécharger justificatif", "Contact", "Voir formations"]
    },
    "comment signaler un problème": {
        "reponse": "Pour signaler un problème technique ou pédagogique, utilise le formulaire de contact ou adresse-toi à l'administration.",
        "suggestions": ["Signaler un problème", "Contact", "Voir formations"]
    },
    "comment participer à un atelier": {
        "reponse": "Les ateliers sont annoncés sur la plateforme et par mail. Inscris-toi via ton espace personnel ou auprès de l'accueil.",
        "suggestions": ["Voir ateliers", "S'inscrire", "Contact"]
    },
    "comment obtenir un reçu de paiement": {
        "reponse": "Un reçu est remis à chaque paiement au centre ou envoyé par mail pour les paiements en ligne.",
        "suggestions": ["Demander un reçu", "Contact", "Voir formations"]
    },
    "comment demander un report de session": {
        "reponse": "Pour reporter ta session, contacte l'administration avant le début du module. Un report est possible sous conditions.",
        "suggestions": ["Demander un report", "Contact", "Voir formations"]
    },
    "comment accéder à la bibliothèque": {
        "reponse": "La bibliothèque GandalHub est ouverte à tous les inscrits. Tu peux y accéder sur place ou en ligne via ton espace personnel.",
        "suggestions": ["Voir bibliothèque", "S'inscrire", "Contact"]
    },
    "comment obtenir un badge de compétence": {
        "reponse": "Un badge numérique est attribué à chaque compétence validée. Tu peux les retrouver dans ton espace personnel.",
        "suggestions": ["Voir mes badges", "Voir formations", "Contact"]
    },
    "comment rejoindre le club des anciens": {
        "reponse": "Le club des anciens est ouvert à tous les diplômés GandalHub. Demande ton accès via l'administration.",
        "suggestions": ["Rejoindre le club", "Contact", "Voir témoignages"]
    },
    "comment parrainer un ami": {
        "reponse": "Parraine un ami et bénéficie d'avantages ! Demande un code de parrainage à l'accueil ou via ton espace personnel.",
        "suggestions": ["Demander un code", "Voir avantages", "Contact"]
    }
}

FAQ_SIMULATION.update({
    # --- Développement Web & JavaScript ---
    "qu'est-ce que le développement web": {
        "reponse": """🌐 Le développement web consiste à créer des sites et applications accessibles via un navigateur (Chrome, Firefox, etc.).
Il inclut :
- Le **frontend** (partie visible, HTML/CSS/JavaScript, frameworks comme React, Vue)
- Le **backend** (partie serveur, Node.js, Python/Django, PHP, bases de données)
- Les API (interfaces pour connecter plusieurs services)
Le développeur web doit aussi connaître l’hébergement, la sécurité, l’accessibilité et le référencement (SEO).
Envie de te lancer ? Je peux te conseiller un parcours adapté !""",
        "suggestions": ["Voir parcours web", "Frontend vs Backend", "S'inscrire"]
    },
    "qu'est-ce que html": {
        "reponse": """📄 **HTML** (HyperText Markup Language) est le langage de base du web. Il sert à structurer le contenu d'une page (titres, paragraphes, images, liens...).
Exemple :
```html
<h1>Titre principal</h1>
<p>Ceci est un paragraphe.</p>
```
HTML ne gère pas le style (c'est le rôle du CSS) ni l'interactivité (c'est le rôle du JavaScript).
Tu veux apprendre à créer ta première page ?""",
        "suggestions": ["Exemple complet", "Cours HTML", "Voir formations web"]
    },
    "qu'est-ce que css": {
        "reponse": """🎨 **CSS** (Cascading Style Sheets) permet de styliser les pages HTML : couleurs, polices, marges, disposition, responsive design...
Exemple :
```css
h1 { color: green; font-size: 2em; }
p { margin-bottom: 10px; }
```
CSS3 apporte des animations, des effets avancés et le support mobile.
Besoin d'un exemple de mise en page ?""",
        "suggestions": ["Exemple CSS", "Cours CSS", "Voir formations web"]
    },
    "qu'est-ce que javascript": {
        "reponse": """💻 **JavaScript** est le langage qui rend les pages web interactives (menus, formulaires, jeux, animations...).
Fonctionne côté navigateur (frontend) et aussi côté serveur (Node.js).
Exemple :
```javascript
document.getElementById('btn').onclick = function() {
  alert('Bouton cliqué !');
}
```
JavaScript est incontournable pour tout développeur web moderne.
Tu veux voir des frameworks JS populaires ?""",
        "suggestions": ["Frameworks JS", "Cours JavaScript", "Voir formations web"]
    },
    "quels sont les frameworks javascript": {
        "reponse": """Les principaux frameworks et bibliothèques JavaScript sont :
- **React.js** (Facebook) : composants réactifs, très utilisé
- **Vue.js** : simple, flexible, populaire en Asie
- **Angular** (Google) : complet, pour grandes applications
- **Node.js** : exécution JS côté serveur
- **Express.js** : framework backend pour Node.js
Chacun a ses avantages selon le projet. Tu veux une comparaison ou un conseil ?""",
        "suggestions": ["React vs Vue", "Node.js", "Cours complet JS"]
    },
    "qu'est-ce que le backend": {
        "reponse": """Le **backend** est la partie serveur d'une application web. Il gère :
- Les bases de données (MySQL, MongoDB, PostgreSQL)
- L’authentification, la sécurité, les API
- La logique métier (traitement des données)
Langages courants : Python (Django, Flask), JavaScript (Node.js), PHP, Java, Ruby.
Tu veux voir un exemple d’API ou de code backend ?""",
        "suggestions": ["Exemple API", "Cours backend", "Voir formations"]
    },
    "qu'est-ce que le frontend": {
        "reponse": """Le **frontend** est la partie visible d’un site web (HTML, CSS, JavaScript). Il s’occupe de l’interface utilisateur, de l’ergonomie et de l’accessibilité.
Les frameworks comme React, Vue, Angular facilitent le développement frontend moderne.
Tu veux apprendre à créer une interface responsive ?""",
        "suggestions": ["Exemple frontend", "Cours HTML/CSS", "Voir formations web"]
    },
    "qu'est-ce qu'une api": {
        "reponse": """Une **API** (Application Programming Interface) permet à deux applications de communiquer entre elles.
Exemple : un site météo utilise l’API d’un service météo pour afficher la température.
Les API sont souvent en format REST (JSON) ou GraphQL.
Tu veux voir comment consommer une API en JavaScript ?""",
        "suggestions": ["Exemple API JS", "Cours API", "Voir formations"]
    },
    "qu'est-ce que la cybersécurité": {
        "reponse": """🔒 La cybersécurité protège les systèmes informatiques contre les attaques, virus, piratages, vols de données.
Principaux domaines :
- Sécurité réseau (pare-feu, VPN, segmentation)
- Sécurité applicative (protection des sites web)
- Sécurité des données (chiffrement, sauvegarde)
- Sensibilisation des utilisateurs (phishing, mots de passe)
Métiers : analyste SOC, pentester, consultant sécurité...
Tu veux des conseils pour sécuriser ton site ou ton réseau ?""",
        "suggestions": ["Conseils sécurité", "Cours cybersécurité", "Voir formations"]
    },
    "qu'est-ce qu'un pare-feu": {
        "reponse": """Un **pare-feu** (firewall) filtre le trafic réseau pour bloquer les connexions non autorisées et protéger les ordinateurs/serveurs.
Il existe des pare-feux matériels (box, routeurs) et logiciels (Windows Defender, UFW sous Linux).
Indispensable pour toute entreprise ou utilisateur connecté.""",
        "suggestions": ["Configurer un pare-feu", "Sécurité réseau", "Voir formations"]
    },
    "qu'est-ce qu'un vpn": {
        "reponse": """Un **VPN** (Virtual Private Network) crée un tunnel sécurisé entre ton appareil et Internet.
Il permet :
- De protéger ta connexion sur les réseaux publics
- D’accéder à distance à un réseau d’entreprise
- De contourner la censure géographique
Exemples : NordVPN, ExpressVPN, OpenVPN.""",
        "suggestions": ["Configurer un VPN", "Sécurité réseau", "Voir formations"]
    },
    "qu'est-ce qu'un pentest": {
        "reponse": """Un **pentest** (test d’intrusion) simule une attaque informatique pour détecter les failles de sécurité d’un système ou d’un site web.
C’est un métier clé en cybersécurité, réalisé par des experts appelés pentesters.""",
        "suggestions": ["Exemple pentest", "Cours cybersécurité", "Voir formations"]
    },
    "qu'est-ce que le réseau informatique": {
        "reponse": """Un **réseau informatique** relie plusieurs ordinateurs et appareils pour partager des données et des ressources (Internet, imprimantes...).
Types de réseaux :
- LAN (Local Area Network) : réseau local (maison, entreprise)
- WAN (Wide Area Network) : réseau étendu (Internet)
- WLAN (Wi-Fi)
Éléments : routeur, switch, câble, point d’accès, etc.""",
        "suggestions": ["Cours réseaux", "Exemple schéma réseau", "Voir formations"]
    },
    "comment devenir développeur web": {
        "reponse": """Pour devenir développeur web :
1. Apprends HTML, CSS, JavaScript (bases du web)
2. Maîtrise un framework moderne (React, Vue, Angular)
3. Découvre le backend (Node.js, Python, PHP)
4. Pratique avec des projets réels (site vitrine, blog, e-commerce)
5. Mets ton code sur GitHub, crée un portfolio
6. Forme-toi en continu (veille technologique)
GandalHub propose un parcours complet pour t’accompagner !""",
        "suggestions": ["Voir parcours web", "S'inscrire", "Voir témoignages"]
    },
    "comment sécuriser un site web": {
        "reponse": """Pour sécuriser un site web :
- Utilise HTTPS (certificat SSL)
- Mets à jour tes logiciels et plugins
- Protège les formulaires (anti-CSRF, captcha)
- Sauvegarde régulièrement tes données
- Utilise des mots de passe forts
- Limite les droits d’accès
- Analyse les logs pour détecter les anomalies
Besoin d’un audit sécurité ?""",
        "suggestions": ["Audit sécurité", "Cours cybersécurité", "Voir formations"]
    },

    # --- Coiffure & Salon ---
    "qu'est-ce que la coiffure": {
        "reponse": """💇‍♀️ La coiffure est l’art de soigner, couper, coiffer et embellir les cheveux.
Techniques :
- Coupe, brushing, coloration, tresses, extensions, lissage, soins capillaires
- Coiffure traditionnelle africaine (nattes, vanilles, tissages)
- Coiffure événementielle (mariage, cérémonies)
Le métier de coiffeur(se) demande créativité, hygiène, sens du contact et formation continue.""",
        "suggestions": ["Voir formation coiffure", "Techniques de tresses", "Ouvrir un salon"]
    },
    "comment ouvrir un salon de coiffure": {
        "reponse": """Pour ouvrir un salon de coiffure :
1. Suivre une formation professionnelle (diplôme ou certificat)
2. Trouver un local adapté (hygiène, accessibilité)
3. Acheter le matériel (fauteuils, bacs, outils, produits)
4. S’enregistrer auprès des autorités (licence, registre)
5. Promouvoir son salon (réseaux sociaux, bouche-à-oreille)
6. Fidéliser la clientèle (qualité, accueil, nouveautés)
GandalHub propose un accompagnement à l’installation !""",
        "suggestions": ["Formation coiffure", "Aide installation", "Contact"]
    },
    "quels sont les outils du coiffeur": {
        "reponse": """Outils essentiels :
- Ciseaux, tondeuse, peignes, brosses
- Sèche-cheveux, lisseur, fer à boucler
- Capes, serviettes, gants
- Produits (shampoing, coloration, soins, gel, mousse)
- Désinfectant, balai, caisse
Un bon entretien du matériel est indispensable pour l’hygiène et la qualité.""",
        "suggestions": ["Liste complète", "Conseils hygiène", "Voir formation"]
    },
    "quelles sont les tendances coiffure en afrique": {
        "reponse": """Tendances actuelles :
- Tresses africaines (box braids, cornrows, twists)
- Nattes collées, vanilles, dreadlocks
- Colorations naturelles, coupes courtes, afro
- Extensions, perruques, lace wigs
- Coiffures événementielles (mariage, baptême)
La coiffure africaine allie tradition et modernité !""",
        "suggestions": ["Exemples en images", "Voir formation", "Contact"]
    },

    # --- Menuiserie ---
    "qu'est-ce que la menuiserie": {
        "reponse": """🪚 La menuiserie est l’art de travailler le bois pour fabriquer des meubles, portes, fenêtres, escaliers, objets décoratifs.
Techniques :
- Découpe, assemblage, ponçage, vernissage
- Utilisation d’outils manuels (scie, rabot, marteau) et machines (scie circulaire, défonceuse)
- Lecture de plans, prise de mesures
Le menuisier doit être précis, créatif et respecter les normes de sécurité.""",
        "suggestions": ["Voir formation menuiserie", "Outils du menuisier", "Contact"]
    },
    "quels sont les outils du menuisier": {
        "reponse": """Outils de base :
- Scie, marteau, rabot, mètre, équerre, tournevis
- Perceuse, ponceuse, visseuse
- Colle à bois, serre-joints, clous, vis
- Équipements de protection (gants, lunettes, masque)
L’utilisation des machines nécessite une formation et des règles de sécurité strictes.""",
        "suggestions": ["Liste complète", "Conseils sécurité", "Voir formation"]
    },
    "comment ouvrir un atelier de menuiserie": {
        "reponse": """Pour ouvrir un atelier :
1. Se former (CAP, certificat, stage)
2. Trouver un local adapté (ventilation, sécurité)
3. Acquérir le matériel et les machines
4. S’enregistrer auprès des autorités
5. Développer un réseau (clients, fournisseurs)
6. Respecter les normes environnementales et de sécurité
GandalHub accompagne les artisans dans leur projet !""",
        "suggestions": ["Formation menuiserie", "Aide installation", "Contact"]
    },

    # --- Pâtisserie ---
    "qu'est-ce que la pâtisserie": {
        "reponse": """🍰 La pâtisserie est l’art de préparer des gâteaux, tartes, viennoiseries, biscuits, desserts.
Techniques :
- Pâtes de base (brisée, feuilletée, sablée)
- Crèmes (pâtissière, chantilly, mousseline)
- Décoration, glaçage, montage
- Respect des dosages, hygiène, créativité
Le métier de pâtissier demande rigueur, précision et passion.""",
        "suggestions": ["Voir formation pâtisserie", "Recettes faciles", "Ouvrir une pâtisserie"]
    },
    "quels sont les outils du pâtissier": {
        "reponse": """Outils indispensables :
- Fouet, spatule, rouleau à pâtisserie, moules, poches à douille
- Balance, tamis, pinceau, grille de refroidissement
- Robot pâtissier, four, plaques
- Thermomètre, emporte-pièces
Un bon pâtissier soigne la présentation et l’hygiène.""",
        "suggestions": ["Liste complète", "Conseils hygiène", "Voir formation"]
    },
    "comment ouvrir une pâtisserie": {
        "reponse": """Pour ouvrir une pâtisserie :
1. Obtenir une formation professionnelle (CAP, certificat)
2. Trouver un local conforme (hygiène, sécurité)
3. Acheter le matériel et les ingrédients
4. S’enregistrer auprès des autorités
5. Créer une gamme de produits (gâteaux, viennoiseries, spécialités locales)
6. Promouvoir son commerce (réseaux sociaux, dégustations)
GandalHub propose une formation complète et un accompagnement à l’installation !""",
        "suggestions": ["Formation pâtisserie", "Aide installation", "Contact"]
    }
})


def get_response(query):
    query = query.lower().strip()

    # Recherche exacte dans la FAQ_SIMULATION
    if query in FAQ_SIMULATION:
        return FAQ_SIMULATION[query]

    # Encouragement et suivi
    if "bravo" in query or "félicitations" in query or "motivation" in query or "encouragement" in query:
        return RESPONSES["encouragement"]
    if "suivant" in query or "continuer" in query or "prochain module" in query or "progression" in query:
        return RESPONSES["proposition_suivi"]

    # Explications techniques (exemple : boucle for en JS)
    if ("boucle" in query or "loop" in query or "pour" in query) and ("javascript" in query or "js" in query or "code" in query):
        return RESPONSES["boucle_js"]

    # Orientation pâtisserie
    if ("apprendre" in query or "formation" in query) and "pâtisserie" in query:
        return RESPONSES["apprendre_patisserie"]

    # Suivi de parcours (exemple : module HTML terminé)
    if ("fini" in query or "terminé" in query or "achevé" in query) and "html" in query:
        return RESPONSES["suivi_html"]

    # Découverte des formations (plus souple)
    if (
        "découvrir" in query or "decouvrir" in query or
        "voir" in query or "liste" in query or
        "formations" in query or "formation" in query
    ):
        return RESPONSES["decouvrir_formations"]

    # Détail sur une formation précise
    for domaine, formations in FORMATIONS.items():
        for key, formation in formations.items():
            if key in query or formation["titre"].lower() in query:
                return RESPONSES[f"formation_{key}"]

    if "bonjour" in query or "salut" in query:
        return RESPONSES["salutation"]
    return RESPONSES["default"]

def suggest_formation(interests):
    suggestions = []
    for domaine, formations in FORMATIONS.items():
        for keyword in interests:
            for key, formation in formations.items():
                if keyword in key or keyword in formation["titre"].lower():
                    suggestions.append((formation["titre"], formation["prix"]))
    return list(set(suggestions))
