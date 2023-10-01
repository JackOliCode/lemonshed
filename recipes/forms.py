from django import forms
from .models import Recipe

CHART__CHOICES = (          #specify choices as a tuple
   ('#1', 'Bar chart'),    # when user selects "Bar chart", it is stored as "#1"
   ('#2', 'Pie chart'),
   ('#3', 'Line chart')
   )

class RecipeSearchForm(forms.Form):
    ingredients = forms.CharField(max_length=350)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'cooking_time', 'ingredients', 'method', 'type', 'pic']