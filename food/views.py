from django.shortcuts import render,redirect,get_object_or_404
from .models import Recipe
from .forms import RecipeForm
from django.contrib import messages
from.forms import SignUpForm
from django.contrib.auth import authenticate, login as auth_login, logout



def recipe_list(request):
    recipes = Recipe.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use auth_login here
            messages.success(request, "You have been Logged in!!")
            return redirect('recips_list')
        else:
            messages.success(request, "There has been an error. Please try again.")
            return redirect('recips_list')
    return render(request, 'recipes.html', {'recipes': recipes})

def about(request):
    return render(request,'about.html')

def login_page(request):
    return render(request, 'login.html')


def add_your_own_recipes(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipe added successfully!')
            return redirect('add_your_own_recipes')
    else:
        form = RecipeForm()
    return render(request, 'add_your_own_recipe.html', {'form': form})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        recipes = Recipe.objects.filter(title__contains=searched)
        return render(request, 'search_results.html', {'searched': searched, 'recipes': recipes})
    else:
        return render(request, 'search_results.html')
    
def register_user(request):
    if request.method == 'POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            auth_login(request,user)
            messages.success(request,"you have successfully registered")
            return redirect('recips_list')
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('login')