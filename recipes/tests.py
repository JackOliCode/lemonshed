from django.test import TestCase
from .models import Recipe
from django.db import models
from django.urls import reverse
from .forms import RecipeSearchForm, AddRecipeForm
from django.contrib.auth.models import User

# Create your tests here.

class RecipeModelTest(TestCase):

    def setUpTestData():
        Recipe.objects.create(name='Smoothie', ingredients='Milk, Banana, Ice Cream', cooking_time='5')

    def test_recipe_name(self):
        recipe_name = Recipe.objects.get(id=1)
        recipe_name_label = recipe_name._meta.get_field('name').verbose_name
        self.assertEqual(recipe_name_label, 'name')

    def test_recipe_ingredients(self):
        ingredients = Recipe.objects.get(id=1)
        recipe_ing_len = ingredients._meta.get_field('ingredients').max_length
        self.assertEqual(recipe_ing_len, 350)

    def test_recipe_cooking_time(self):
        cooking_time = Recipe.objects.get(id=1)
        recipe_cooking_time = cooking_time._meta.get_field('cooking_time')
        self.assertIsInstance(recipe_cooking_time, models.FloatField)

    def test_get_absolute_url(self):
       recipe = Recipe.objects.get(id=1)
       #get_absolute_url() should take you to the detail page of recipe #1
       #and load the URL /books/list/1
       self.assertEqual(recipe.get_absolute_url(), '/list/1')


class RecipeFormTest(TestCase):
    def test_recipe_search_form_valid(self):
        form_data = {
            'ingredients': 'Ingredient1 Ingredient2',
            'chart_type': '#1',
        }
        form = RecipeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_recipe_search_form_invalid(self):
        form_data = {}  # Invalid data with missing required fields
        form = RecipeSearchForm(data=form_data)
        self.assertFalse(form.is_valid())

class SearchViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_search_view_with_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('recipes:search'), {
            'ingredients': 'milk',
            'chart_type': '#1',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'milk')
        self.assertContains(response, 'Chart')

    
class AddRecipeViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_add_recipe_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('recipes:add-recipe'))  # Updated view name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/add-recipe.html')
        self.assertIsInstance(response.context['form'], AddRecipeForm)

    
    def test_add_recipe_post_invalid_data(self):
        self.client.login(username='testuser', password='testpassword')
        post_data = {}  # Provide invalid form data
        response = self.client.post(reverse('recipes:add-recipe'), post_data)  # Updated view name
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], AddRecipeForm)

class AboutMeViewTest(TestCase):
    def test_about_me_get(self):
        response = self.client.get(reverse('recipes:about-me'))  # Use the correct view name with the app namespace
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/about-me.html')    