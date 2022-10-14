# Generated by Django 4.0 on 2022-10-13 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishe_1', models.CharField(max_length=255)),
                ('dishe_2', models.CharField(blank=True, max_length=255, null=True)),
                ('dishe_3', models.CharField(blank=True, max_length=255, null=True)),
                ('dishe_4', models.CharField(blank=True, max_length=255, null=True)),
                ('dishe_5', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Ingrediente',
                'verbose_name_plural': 'ingredientes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RecipesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipes/img')),
                ('link_video', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.CharField(choices=[('V', 'vegana'), ('C', 'Carnes'), ('P', 'Postres'), ('S', 'SinTacc'), ('PA', 'Pastas')], max_length=12)),
                ('number_of_dishes', models.IntegerField()),
                ('timeday', models.CharField(blank=True, choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], max_length=12, null=True)),
                ('recipes_time', models.IntegerField()),
                ('like', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredients')),
            ],
            options={
                'verbose_name': 'Recipe',
                'verbose_name_plural': 'Recipes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredients')),
                ('platillo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipesmodel')),
            ],
            options={
                'verbose_name': 'Favorito',
                'verbose_name_plural': 'Favoritos',
                'ordering': ['id'],
            },
        ),
    ]