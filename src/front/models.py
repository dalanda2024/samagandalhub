from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class CustomUser(AbstractUser):
    is_formateur = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

class Cours(models.Model):
    CATEGORIES = [
        ('cuisine', 'Cuisine'),
        ('patisserie', 'Pâtisserie'),
        ('entreprenariat', 'Entreprenariat'),
        ('makeup', 'Makeup'),
        ('couture', 'Couture'),
        ('developpement personnel', 'Développement personnel'),
        ('informatique', 'Informatique'),
        ('reseau', 'Réseau'),
        ('gestion de projet', 'Gestion de projet'),
    ]

    titre = models.CharField(max_length=255)
    description = models.TextField()
    categorie = models.CharField(max_length=50, choices=CATEGORIES)
    image = models.ImageField(upload_to='cours/')
    formateur = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="cours_donnes")
    date_publication = models.DateTimeField(auto_now_add=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # ✅ Ajout du champ prix


class Module(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='modules')
    ordre = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.titre

class Progression(models.Model):
    utilisateur = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    terminee = models.BooleanField(default=False)
    date_debut = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(null=True, blank=True)

class EvenementBlog(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_evenement = models.DateField()
    image = models.ImageField(upload_to="evenements/", null=True, blank=True)
    auteur = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    type = models.CharField(choices=[('blog', 'Blog'), ('evenement', 'Événement')], max_length=10)

# Quiz
class Quiz(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    question = models.TextField(default="Question à définir")  # Ajout du default ici

    def __str__(self):
        return f"{self.module.titre} - {self.question[:50]}"



class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    texte = models.CharField(max_length=500)

    def __str__(self):
        return self.texte

class Choix(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choix')
    texte = models.CharField(max_length=300)
    est_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.texte

class ReponseUtilisateur(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choix = models.ForeignKey(Choix, on_delete=models.CASCADE)
    date_reponse = models.DateTimeField(auto_now_add=True)