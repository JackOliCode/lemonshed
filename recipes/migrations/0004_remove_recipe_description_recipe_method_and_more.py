# Generated by Django 4.2.4 on 2023-09-08 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_description_recipe_pic_recipe_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='description',
        ),
        migrations.AddField(
            model_name='recipe',
            name='method',
            field=models.TextField(default='The method for this recipe is coming soon', max_length=200),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='type',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('snack', 'Snack'), ('drink', 'Drink'), ('other', 'Other')], default='other', max_length=9),
        ),
    ]
