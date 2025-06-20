from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from front.models import Cours
from django.core.files.images import ImageFile
import os
from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    help = 'Création des cours avec leurs formateurs'

    def handle(self, *args, **kwargs):
        # Création des instructeurs si nécessaires
        instructors = [
            {'username': 'chef_aminata', 'first_name': 'Aminata', 'last_name': 'Diallo'},
            {'username': 'fatoumata_b', 'first_name': 'Fatoumata', 'last_name': 'B.'},
            {'username': 'mariam_d', 'first_name': 'Mariam', 'last_name': 'D.'},
            {'username': 'chef_oumar', 'first_name': 'Oumar', 'last_name': 'S.'},
            {'username': 'ibrahima_k', 'first_name': 'Ibrahima', 'last_name': 'K.'},
            {'username': 'aissatou_d', 'first_name': 'Aissatou', 'last_name': 'D.'},
            {'username': 'mohamed_c', 'first_name': 'Mohamed', 'last_name': 'C.'},
            {'username': 'mamadou_b', 'first_name': 'Mamadou', 'last_name': 'B.'},
            {'username': 'fatou_n', 'first_name': 'Fatou', 'last_name': 'N.'},
        ]

        for instr in instructors:
            User.objects.get_or_create(
                username=instr['username'],
                defaults={
                    'first_name': instr['first_name'],
                    'last_name': instr['last_name'],
                    'email': f"{instr['username']}@gandlhub.com",
                    'password': 'password123',
                    'is_formateur': True
                }
            )
            self.stdout.write(f"Instructeur créé ou existant : {instr['username']}")

        # Création des cours avec descriptions détaillées
        courses_data = [
            {
                'titre': 'Cuisine Africaine Traditionnelle',
                'categorie': 'cuisine',
                'instructeur': 'chef_aminata',
                'description': (
                    "Découvrez et maîtrisez les plats emblématiques de la cuisine africaine, "
                    "de la préparation des ingrédients locaux aux techniques traditionnelles de cuisson. "
                    "Ce cours vous guidera dans la création de recettes savoureuses et authentiques, "
                    "incluant des spécialités régionales qui raviront vos convives."
                ),
                'prix': 99000,
                'image_path': 'img/CuisineAfricaineTraditionnelle.jpg'
            },
            {
                'titre': 'Maquillage Professionnel',
                'categorie': 'makeup',
                'instructeur': 'fatoumata_b',
                'description': (
                    "Apprenez les techniques avancées du maquillage professionnel adaptées à tous types de peau. "
                    "Ce cours couvre le maquillage de jour, de soirée, et les tendances actuelles, "
                    "ainsi que les conseils pour sublimer les traits naturels et utiliser correctement les produits."
                ),
                'prix': 75000,
                'image_path': 'img/MaquillageProfessionnel.jpg'
            },
            {
                'titre': 'Couture Moderne Africaine',
                'categorie': 'couture',
                'instructeur': 'mariam_d',
                'description': (
                    "Explorez la création de vêtements modernes et élégants inspirés par les tissus et motifs africains. "
                    "Apprenez à concevoir, couper, assembler et personnaliser vos créations, "
                    "alliant traditions artisanales et styles contemporains pour un résultat unique."
                ),
                'prix': 120000,
                'image_path': 'img/CoutureModerneAfricaine.jpg'
            },
            {
                'titre': 'Pâtisserie Africaine',
                'categorie': 'patisserie',
                'instructeur': 'chef_oumar',
                'description': (
                    "Découvrez l’art de la pâtisserie africaine, mêlant recettes traditionnelles et innovations modernes. "
                    "Ce cours vous fera maîtriser la préparation de desserts typiques, gâteaux, biscuits et douceurs exquises, "
                    "avec un focus sur les ingrédients locaux et les techniques de cuisson adaptées."
                ),
                'prix': 85000,
                'image_path': 'img/PatisserieAfricaine.jpg'
            },
            {
                'titre': 'Bureautique Essentielle',
                'categorie': 'informatique',
                'instructeur': 'ibrahima_k',
                'description': (
                    "Maîtrisez les logiciels incontournables du pack Office : Word, Excel et PowerPoint. "
                    "Ce cours vous permettra de créer des documents professionnels, gérer des tableaux complexes, "
                    "et réaliser des présentations efficaces et dynamiques."
                ),
                'prix': 150000,
                'image_path': 'img/BureautiqueEssentielle.jpg'
            },
            {
                'titre': 'Gestion de Projet Agile',
                'categorie': 'gestion de projet',
                'instructeur': 'aissatou_d',
                'description': (
                    "Apprenez à piloter vos projets avec les méthodes agiles, favorisant flexibilité et collaboration. "
                    "Ce cours couvre les principes Scrum, Kanban, et autres techniques, "
                    "avec des outils pratiques pour planifier, suivre et ajuster vos projets en temps réel."
                ),
                'prix': 200000,
                'image_path': 'img/GestiondeProjetAgile.jpg'
            },
            {
                'titre': 'Réseaux Informatiques',
                'categorie': 'reseau',
                'instructeur': 'mohamed_c',
                'description': (
                    "Initiez-vous à la conception, configuration et administration des réseaux informatiques. "
                    "Ce cours vous guide à travers les protocoles, topologies, sécurités, et outils indispensables "
                    "pour gérer efficacement un réseau professionnel."
                ),
                'prix': 250000,
                'image_path': 'img/RéseauxInformatiques.jpg'
            },
            {
                'titre': 'Développement Personnel',
                'categorie': 'developpement personnel',
                'instructeur': 'mamadou_b',
                'description': (
                    "Boostez votre confiance en vous et améliorez vos compétences en communication. "
                    "Ce cours propose des exercices pratiques pour mieux gérer le stress, "
                    "fixer des objectifs clairs, et développer un état d’esprit positif dans votre vie personnelle et professionnelle."
                ),
                'prix': 80000,
                'image_path': 'img/DéveloppementPersonnel.jpg'
            },
            {
                'titre': 'Lancez Votre Startup',
                'categorie': 'entreprenariat',
                'instructeur': 'fatou_n',
                'description': (
                    "Découvrez toutes les étapes essentielles pour créer et développer votre startup. "
                    "De l’idée initiale au business plan, en passant par le financement, le marketing et la gestion, "
                    "ce cours vous prépare à réussir votre aventure entrepreneuriale."
                ),
                'prix': 180000,
                'image_path': 'img/Entreprenariat.jpg'
            }
        ]

        for data in courses_data:
            try:
                formateur = User.objects.get(username=data['instructeur'])

                cours, created = Cours.objects.get_or_create(
                    titre=data['titre'],
                    defaults={
                        'categorie': data['categorie'],
                        'formateur': formateur,
                        'description': data['description'],
                        'prix': data['prix']
                    }
                )

                if not created:
                    # Forcer la mise à jour des champs même si le cours existe déjà
                    cours.categorie = data['categorie']
                    cours.formateur = formateur
                    cours.description = data['description']
                    cours.prix = data['prix']
                    cours.save()

                # Toujours forcer la sauvegarde / mise à jour de l'image
                image_path = os.path.join(settings.BASE_DIR, 'front', 'static', data['image_path'])
                if os.path.exists(image_path):
                    with open(image_path, 'rb') as f:
                        if cours.image:
                            cours.image.delete(save=False)
                        cours.image.save(os.path.basename(image_path), ImageFile(f), save=True)
                    self.stdout.write(self.style.SUCCESS(f"Image ajoutée pour le cours : {data['titre']}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Image non trouvée : {image_path}"))

                self.stdout.write(self.style.SUCCESS(f"Cours {'créé' if created else 'mis à jour'} : {data['titre']}"))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Erreur avec {data['titre']}: {str(e)}"))
