from django.db import models
from django.shortcuts import reverse

meal_type_choices=(
('Breakfast','Breakfast'),
('Lunch', 'Lunch'),
('Dinner', 'Dinner'),
('Snack', 'Snack'),
('Drink', 'Drink'),
('Other', 'Other')
)

#model below
class Recipe (models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text='in minutes')
    ingredients = models.CharField(max_length=350)
    method = models.TextField(max_length=5000, default='The method for this recipe is coming soon')
    type = models.CharField(max_length=9, choices=meal_type_choices, default='Other')
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    # calc difficulty function

    def calculate_difficulty(self):
            num_ingredients = len(self.ingredients.split(','))
            if self.cooking_time < 10:
                if num_ingredients < 4:
                    difficulty = "Easy"
                else:
                    difficulty = "Medium"
            else:
                if num_ingredients < 4:
                    difficulty = "Intermediate"
                else:
                    difficulty = "Hard"

            return difficulty
    
    def get_absolute_url(self):
       return reverse ('recipes:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.name)
