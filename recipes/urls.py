from django.urls import path
from .views import welcome
from .views import RecipeListView
from .views import RecipeDetailView
from .views import search
from .views import add_recipe
from .views import about_me
app_name = 'recipes'

urlpatterns = [
   path('', welcome),
   path('list/', RecipeListView.as_view(), name='list'),
   path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
   path('search/', search, name='search'),
   path('add/', add_recipe, name='add-recipe'),
   path('about/', about_me, name='about-me'),
]