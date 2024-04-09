# views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Recipe
from .forms import RecipeForm
def base(request):
    return render(request, 'base.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already taken'})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')  
    return render(request, 'signup.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')
def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})

def logout_view(request):
    logout(request)
    return redirect('base')


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'create_recipe.html', {'form': form})



def base(request):
    recipes = Recipe.objects.all()
    return render(request, 'base.html', {'recipes': recipes})



def remove_recipe(request):
    if request.method == 'POST':
        recipe_id = request.POST.get('recipe_id')
        if recipe_id:
            try:
                recipe = get_object_or_404(Recipe, id=recipe_id)
                recipe.delete()
            except Recipe.DoesNotExist:
                # Handle case where recipe with given ID does not exist
                pass
    return redirect('home')

def edit_recipe(request):
    if request.method == 'POST':
        recipe_id = request.POST.get('recipe_id')
        recipe = Recipe.objects.get(id=recipe_id)
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')  # Assuming 'home' is the name of your home page URL pattern
    else:
        recipe_id = request.GET.get('recipe_id')
        recipe = Recipe.objects.get(id=recipe_id)
        form = RecipeForm(instance=recipe)
    return render(request, 'edit_recipe.html', {'form': form})

