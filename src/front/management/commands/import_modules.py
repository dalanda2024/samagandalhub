from django.core.management.base import BaseCommand
from front.models import Cours, Module

class Command(BaseCommand):
    help = "Ajoute ou met à jour les modules pour chaque cours de formation"

    def handle(self, *args, **kwargs):
        # Dictionnaire des cours et leurs modules associés
        modules_data = {
            "Cuisine Africaine Traditionnelle": [
                {
                    "ordre": 1,
                    "titre": "Introduction à la cuisine africaine",
                    "contenu": "Présentation des ingrédients typiques, des épices locales et de l'histoire culinaire africaine. "
                               "Vous apprendrez l'importance culturelle de chaque ingrédient et leur utilisation dans les plats traditionnels."
                },
                {
                    "ordre": 2,
                    "titre": "Plats principaux emblématiques",
                    "contenu": "Réalisation des plats comme le maffé, le yassa, le fonio, etc. Apprentissage des techniques de cuisson traditionnelles."
                },
                {
                    "ordre": 3,
                    "titre": "Astuces et présentation",
                    "contenu": "Techniques de dressage, présentation esthétique et astuces pour réussir chaque plat comme un chef professionnel."
                },
            ],
            "Maquillage Professionnel": [
                {
                    "ordre": 1,
                    "titre": "Bases du maquillage",
                    "contenu": "Comprendre les types de peaux, préparer le visage, choisir les produits adaptés (fond de teint, anti-cernes, etc)."
                },
                {
                    "ordre": 2,
                    "titre": "Maquillage de jour et de nuit",
                    "contenu": "Réaliser un maquillage naturel pour le jour et un look glamour pour la soirée. Techniques d’application et choix des couleurs."
                },
            ],
            "Couture Moderne Africaine": [
                {
                    "ordre": 1,
                    "titre": "Techniques de coupe",
                    "contenu": "Apprentissage de la découpe selon les tissus africains (pagne, bazin...) et des patrons de couture modernes."
                },
                {
                    "ordre": 2,
                    "titre": "Assemblage et finitions",
                    "contenu": "Assembler les différentes pièces du vêtement et faire les finitions comme un professionnel."
                },
            ],
            "Pâtisserie Africaine": [
                {
                    "ordre": 1,
                    "titre": "Gâteaux traditionnels",
                    "contenu": "Préparer des desserts locaux comme le thiakry, les beignets, les galettes et autres douceurs typiques africaines."
                },
                {
                    "ordre": 2,
                    "titre": "Recettes modernes inspirées",
                    "contenu": "Créer des pâtisseries modernes inspirées de recettes africaines, avec des touches innovantes."
                },
            ],
            "Bureautique Essentielle": [
                {
                    "ordre": 1,
                    "titre": "Microsoft Word",
                    "contenu": "Création, mise en forme, insertion d'images et tableaux, gestion des styles et mise en page de documents professionnels."
                },
                {
                    "ordre": 2,
                    "titre": "Microsoft Excel",
                    "contenu": "Création de feuilles de calcul, formules de base et avancées, tableaux croisés dynamiques, graphiques."
                },
                {
                    "ordre": 3,
                    "titre": "Microsoft PowerPoint",
                    "contenu": "Réalisation de présentations dynamiques avec animations, transitions, insertion de contenus multimédias."
                },
            ],
            "Gestion de Projet Agile": [
                {
                    "ordre": 1,
                    "titre": "Introduction à l'agilité",
                    "contenu": "Comprendre les méthodes agiles (Scrum, Kanban), les valeurs du manifeste agile et les rôles clés."
                },
                {
                    "ordre": 2,
                    "titre": "Sprints et backlog",
                    "contenu": "Apprendre à planifier un sprint, gérer un backlog produit, faire un daily meeting, utiliser les outils agiles."
                },
            ],
            "Réseaux Informatiques": [
                {
                    "ordre": 1,
                    "titre": "Modèles OSI et TCP/IP",
                    "contenu": "Découverte des couches réseau et de leur rôle dans la communication entre les ordinateurs."
                },
                {
                    "ordre": 2,
                    "titre": "Configuration de routeurs",
                    "contenu": "Configurer un routeur, un switch, créer un réseau local sécurisé et surveiller son fonctionnement."
                },
            ],
            "Développement Personnel": [
                {
                    "ordre": 1,
                    "titre": "Estime de soi",
                    "contenu": "Développer la confiance en soi, s’accepter, se fixer des objectifs personnels et professionnels."
                },
                {
                    "ordre": 2,
                    "titre": "Communication efficace",
                    "contenu": "Techniques pour bien s’exprimer à l’oral et à l’écrit, améliorer ses relations interpersonnelles."
                },
            ],
            "Lancez Votre Startup": [
                {
                    "ordre": 1,
                    "titre": "Idéation et validation",
                    "contenu": "Trouver une idée de startup, analyser le marché, identifier ses clients cibles, tester l’idée avec des MVP."
                },
                {
                    "ordre": 2,
                    "titre": "Business Plan et levée de fonds",
                    "contenu": "Rédiger un business plan complet, présenter son projet à des investisseurs, obtenir des financements."
                },
            ],
        }

        for titre_cours, modules in modules_data.items():
            try:
                cours = Cours.objects.get(titre=titre_cours)
                for mod in modules:
                    # Recherche du module existant ou création
                    module, created = Module.objects.get_or_create(
                        cours=cours,
                        ordre=mod["ordre"],
                        defaults={
                            "titre": mod["titre"],
                            "contenu": mod["contenu"]
                        }
                    )
                    # Mise à jour forcée même si le module existe déjà
                    if not created:
                        module.titre = mod["titre"]
                        module.contenu = mod["contenu"]
                        module.save()
                        self.stdout.write(self.style.WARNING(f"Module mis à jour : {module.titre} - {cours.titre}"))
                    else:
                        self.stdout.write(self.style.SUCCESS(f"Module créé : {module.titre} - {cours.titre}"))
            except Cours.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Cours non trouvé : {titre_cours}"))
