from django.core.management.base import BaseCommand
from front.models import Module, Quiz

class Command(BaseCommand):
    help = "Ajoute automatiquement les quiz pour chaque module existant"

    def handle(self, *args, **kwargs):
        quiz_data = {
            "Introduction à la cuisine africaine": [
                "Quels sont les ingrédients de base de la cuisine africaine ?",
                "Pourquoi certaines épices sont-elles utilisées dans la tradition ?",
            ],
            "Plats principaux emblématiques": [
                "Quel plat est originaire du Sénégal ?",
                "Quelles sont les étapes de cuisson du Maffé ?",
            ],
            "Bases du maquillage": [
                "Quel type de peau nécessite une base hydratante ?",
                "Quels sont les outils essentiels pour appliquer le fond de teint ?",
            ],
            "Techniques de coupe": [
                "Quel tissu africain est le plus utilisé pour les tenues de cérémonie ?",
                "Pourquoi faut-il laver le tissu avant de le découper ?",
            ],
            "Gâteaux traditionnels": [
                "Quels sont les ingrédients du Thiakry ?",
                "Quelle est la différence entre un beignet africain et un donut occidental ?",
            ],
            "Microsoft Word": [
                "Comment insérer une table des matières ?",
                "Quelle est la fonction du volet de navigation ?",
            ],
            "Introduction à l'agilité": [
                "Quels sont les 4 valeurs du manifeste agile ?",
                "Quels rôles sont présents dans une équipe Scrum ?",
            ],
            "Modèles OSI et TCP/IP": [
                "Combien de couches possède le modèle OSI ?",
                "Quelle couche gère le routage dans TCP/IP ?",
            ],
            "Estime de soi": [
                "Citez trois techniques pour améliorer l’estime de soi.",
                "Pourquoi est-il important de se fixer des objectifs ?",
            ],
            "Idéation et validation": [
                "Qu'est-ce qu'un MVP en startup ?",
                "Comment valider une idée de produit avec peu de moyens ?",
            ],
        }

        for titre_module, questions in quiz_data.items():
            try:
                module = Module.objects.get(titre=titre_module)
                for question_text in questions:
                    quiz, created = Quiz.objects.get_or_create(
                        module=module,
                        question=question_text
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Quiz ajouté : {question_text} (Module : {titre_module})"))
                    else:
                        self.stdout.write(self.style.WARNING(f"Quiz déjà existant : {question_text} (Module : {titre_module})"))
            except Module.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Module non trouvé : {titre_module}"))
