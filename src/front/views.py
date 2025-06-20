from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import Http404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import CustomUserCreationForm, CustomLoginForm, ProfileUpdateForm ,CoursForm, EvenementForm, FormateurForm
from .models import Cours, Module, EvenementBlog, CustomUser, Progression, Quiz, ReponseUtilisateur
from django.contrib import messages
from django.db.models import Q




def is_admin(user):
    return user.is_authenticated and user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_ajouter_module(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Module ajouté avec succès.")
            return redirect('admin_cours')  # ou admin_modules si tu crées cette page
    else:
        form = ModuleForm()
    return render(request, 'dashboard/ajouter_module.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    total_users = CustomUser.objects.count()
    total_formateurs = CustomUser.objects.filter(is_formateur=True).count()
    total_cours = Cours.objects.count()
    total_evenements = EvenementBlog.objects.count()
    return render(request, 'dashboard/dashboard.html', {
        'total_users': total_users,
        'total_formateurs': total_formateurs,
        'total_cours': total_cours,
        'total_evenements': total_evenements,
    })

@login_required
@user_passes_test(is_admin)
def admin_utilisateurs(request):
    utilisateurs = CustomUser.objects.all()
    return render(request, 'dashboard/utilisateurs.html', {'utilisateurs': utilisateurs})

@login_required
@user_passes_test(is_admin)
def admin_cours(request):
    cours = Cours.objects.all()
    return render(request, 'dashboard/cours.html', {'cours': cours})

@login_required
@user_passes_test(is_admin)
def admin_ajouter_cours(request):
    if request.method == 'POST':
        form = CoursForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cours ajouté avec succès.')
            return redirect('admin_cours')
    else:
        form = CoursForm()
    return render(request, 'dashboard/ajouter_cours.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def admin_cours_detail(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    return render(request, 'dashboard/cours_detail.html', {'cours': cours})

@login_required
@user_passes_test(is_admin)
def admin_evenements(request):
    evenements = EvenementBlog.objects.all()
    return render(request, 'dashboard/evenements.html', {'evenements': evenements})

@login_required
@user_passes_test(is_admin)
def admin_ajouter_evenement(request):
    if request.method == 'POST':
        form = EvenementForm(request.POST, request.FILES)
        if form.is_valid():
            evenement = form.save(commit=False)
            evenement.auteur = request.user
            evenement.save()
            messages.success(request, 'Événement ajouté avec succès.')
            return redirect('admin_evenements')
    else:
        form = EvenementForm()
    return render(request, 'dashboard/ajouter_evenement.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def admin_ajouter_formateur(request):
    if request.method == 'POST':
        form = FormateurForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_formateur = True
            user.save()
            messages.success(request, 'Formateur ajouté avec succès.')
            return redirect('admin_utilisateurs')
    else:
        form = FormateurForm()
    return render(request, 'dashboard/ajouter_formateur.html', {'form': form})

# modifier et supprimer un cours
@login_required
@user_passes_test(is_admin)
def course_edit(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    if request.method == 'POST':
        form = CoursForm(request.POST, request.FILES, instance=cours)
        if form.is_valid():
            form.save()
            messages.success(request, "Cours mis à jour avec succès.")
            return redirect('admin_cours')
    else:
        form = CoursForm(instance=cours)
    return render(request, 'dashboard/course_edit.html', {'form': form, 'cours': cours})

@login_required
@user_passes_test(is_admin)
def course_delete(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    if request.method == 'POST':
        cours.delete()
        messages.success(request, "Cours supprimé avec succès.")
        return redirect('admin_cours')
    return render(request, 'dashboard/course_confirm_delete.html', {'cours': cours})


# Utiisateurs
@login_required
def dashboard_utilisateur(request):
    utilisateur = request.user
    cours_utilisateur = Cours.objects.filter(formateur=utilisateur)
    formateurs = CustomUser.objects.filter(is_formateur=True)
    evenements = EvenementBlog.objects.all().order_by('-date_evenement')

    return render(request, 'dashboard/dashboard_utilisateur.html', {
        'cours_utilisateur': cours_utilisateur,
        'formateurs': formateurs,
        'evenements': evenements,
    })

def redirection_post_login(request):
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    else:
        return redirect('course_list')




def index(request):
    return render(request, 'front/index.html')

def about(request):
    return render(request, 'front/about.html')

def contact(request):
    return render(request, 'front/contact.html')

# def course_detail(request):
#     return render(request, 'front/course_detail.html')


def events(request):
    return render(request, 'front/events.html')


def pricing(request):
    return render(request, 'front/pricing.html')

def trainer_profile(request):
    return render(request, 'front/trainers.html')

def trainers(request):
    return render(request, 'front/trainers.html')


# --------- FORMATEUR - GESTION MODULES ---------
@login_required
def ajouter_module(request, cours_id):
    cours = get_object_or_404(Cours, pk=cours_id, formateur=request.user)
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            module = form.save(commit=False)
            module.cours = cours
            module.save()
            messages.success(request, 'Module ajouté.')
            return redirect('course_details', pk=cours.id)
    else:
        form = ModuleForm()
    return render(request, 'dashboard/ajouter_module.html', {'form': form, 'cours': cours})

# --------- UTILISATEUR - SUIVI DE PROGRESSION ---------
@login_required
def suivre_module(request, module_id):
    module = get_object_or_404(Module, pk=module_id)
    progression, created = Progression.objects.get_or_create(
        utilisateur=request.user,
        module=module,
        defaults={'terminee': True}
    )
    if not created:
        progression.terminee = not progression.terminee
        progression.save()
    return redirect('front/course_detail', pk=module.cours.id)



def course_list(request):
    query = request.GET.get('search', '')
    categorie = request.GET.get('categorie', '')
    cours = Cours.objects.all()

    if query:
        cours = cours.filter(Q(titre__icontains=query) | Q(description__icontains=query))

    if categorie:
        cours = cours.filter(categorie=categorie)

    categories = [
        'cuisine', 'patisserie', 'entreprenariat', 'makeup', 'couture',
        'developpement personnel', 'informatique', 'reseau', 'gestion de projet'
    ]

    return render(request, 'front/course_list.html', {
        'cours': cours,
        'categories': categories,
    })

def course_detail(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    modules = cours.modules.all()
    progression = None

    if request.user.is_authenticated:
        progression = {
            module.pk: Progression.objects.filter(module=module, utilisateur=request.user, terminee=True).exists()
            for module in modules
        }

    first_module = modules.first() if modules else None

    return render(request, 'front/course_detail.html', {
        'cours': cours,
        'modules': modules,
        'progression': progression,
        'first_module': first_module,
    })



def register_view(request):
    if request.method == 'POST':
        print("Formulaire reçu")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Formulaire valide")
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie.")
            return redirect('index')
        else:
            print("Formulaire invalide")
            print(form.errors)  # 👈 ajoute cette ligne pour voir les erreurs
    else:
        form = CustomUserCreationForm()
    return render(request, 'front/register.html', {'form': form})
    


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Connexion réussie.")
            return redirection_post_login(request)
        else:
            messages.error(request, "Identifiants incorrects. Veuillez réessayer.")
    else:
        form = CustomLoginForm()
    return render(request, 'front/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect('index')

@login_required
def courses(request):
    cours = Cours.objects.filter(formateur=request.user) if request.user.is_formateur else Cours.objects.all()
    return render(request, 'front/courses.html', {'cours': cours})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profil mis à jour.")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'front/profile.html', {'form': form})


# Module
def voir_module(request, pk):
    module = get_object_or_404(Module, pk=pk)
    quiz = Quiz.objects.filter(module=module).first()

    return render(request, 'front/module_detail.html', {
        'module': module,
        'quiz': quiz,
    })

@login_required
def marquer_termine(request, pk):
    module = get_object_or_404(Module, pk=pk)
    progression, created = Progression.objects.get_or_create(module=module, utilisateur=request.user)
    progression.terminee = True
    progression.save()
    return redirect('voir_module', pk=pk)

# Quiz
def quiz_module(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    quiz = module.quiz_set.first()  # Un seul quiz par module attendu

    if not quiz:
        return render(request, 'front/quiz_module.html', {
            'module': module,
            'questions': [],
            'quiz': None,
            'error': 'Aucun quiz trouvé pour ce module.'
        })

    questions = quiz.questions.prefetch_related('choix')

    if request.method == "POST":
        score = 0
        total = questions.count()

        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected:
                choix = question.choix.get(id=selected)
                ReponseUtilisateur.objects.update_or_create(
                    utilisateur=request.user,
                    question=question,
                    defaults={'choix': choix}
                )
                if choix.est_correct:
                    score += 1

        return render(request, 'front/quiz_result.html', {
            'module': module,
            'score': score,
            'total': total
        })

    return render(request, 'front/quiz_module.html', {
        'module': module,
        'quiz': quiz,
        'questions': questions
    })


# payement
def valider_paiement(request):
    if request.method == 'POST':
        mode = request.POST.get('mode_paiement')

        if mode == 'orange':
            phone = request.POST.get('orange_phone')
            code = request.POST.get('orange_code')
            # Traitement Orange Money
        elif mode == 'mtn':
            phone = request.POST.get('mtn_phone')
            code = request.POST.get('mtn_code')
            # Traitement MTN Money
        elif mode == 'card':
            number = request.POST.get('card_number')
            name = request.POST.get('card_name')
            expiry = request.POST.get('card_expiry')
            cvv = request.POST.get('card_cvv')
            # Traitement Carte Bancaire

        # Logique commune après paiement
        return redirect('confirmation_paiement')
