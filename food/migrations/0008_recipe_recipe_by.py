# Generated by Django 4.2 on 2023-09-02 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_remove_recipe_recipe_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_by',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
    ]
