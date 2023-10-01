from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm
import pandas as pd
from django.db.models import Q
from .utils import get_chart
from. forms import AddRecipeForm
# Create your views here.

def welcome(request):
    return render(request, 'recipes/login.html')


####### search function 

@login_required
def search(request):
    form = RecipeSearchForm(request.POST or None)
    recipes_df = None #initialize dataframe to None
    chart = None

    if request.method == 'POST':
        ingredients = request.POST.get('ingredients')
        chart_type = request.POST.get('chart_type')

       ### Split the input into keywords ###
        keywords = ingredients.split()

        ### Create a Q object (encapsualtes multiple conditions)
        query = Q()
        for keyword in keywords:
            query |= Q(ingredients__icontains=keyword)

        #apply filter to extract data
        qs =Recipe.objects.filter(query)
        if qs:
            data = {
                'Name': [recipe.name for recipe in qs],
                'Cooking Time': [recipe.cooking_time for recipe in qs],
                'Ingredients': [recipe.ingredients for recipe in qs],
                'Type': [recipe.type for recipe in qs],
                'Difficulty': [recipe.calculate_difficulty() for recipe in qs],
            }
            recipes_df = pd.DataFrame(data)
            chart=get_chart(chart_type, recipes_df, labels=recipes_df['Cooking Time'].values)
            recipes_df=recipes_df.to_html()
            
        for recipe in qs:
            recipes_df = recipes_df.replace(
            f"<td>{recipe.name}</td>",
            f'<td><a href="/list/{recipe.id}">{recipe.name}</a></td>',
        )

    context={
        'form': form,
        'recipes_df': recipes_df,
        'chart': chart
    }

    return render(request, 'recipes/search.html', context)

#=================
#Add new recipe
#================
@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('recipes:list')
    else:
        form = AddRecipeForm()

    return render(request, 'recipes/add-recipe.html', {'form': form})

#=================
#About me
#================
def about_me(request):
    return render(request, 'recipes/about-me.html')



class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/home.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'
