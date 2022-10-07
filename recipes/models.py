from django.db import models


#Tabla ingredientes relacionada con RecipesModel para traer nombre de receta
class Ingredients(models.Model):
    dishe_1= models.CharField(max_length=255)
    dishe_2= models.CharField(max_length=255, blank=True, null=True)
    dishe_3= models.CharField(max_length=255, blank=True, null=True)
    dishe_4= models.CharField(max_length=255, blank=True, null=True)
    dishe_5= models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"ingrediente-> {self.dishe_1}"
    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'ingredientes'
        ordering = ['id']

# Create your models here.
class RecipesModel(models.Model):
    time_choice = [
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner')
    ]
    category_choice=[
        ('V','vegana'),
        ('C', 'Carnes'),
        ('P','Postres'),
        ('S', 'SinTacc'),
        ('PA', 'Pastas')
    ]
    title=models.CharField(max_length=255, unique=True)
    image=models.ImageField(upload_to="recipes/img", blank=True, null=True)
    link_video=models.CharField(max_length=255, blank=True, null=True)
    category=models.CharField(max_length=12, choices=category_choice)
    number_of_dishes=models.IntegerField()
    timeday= models.CharField(max_length=12,choices=time_choice, null=True, blank=True)
    recipes_time=models.IntegerField()
    ingredients=models.ManyToManyField(Ingredients)
    like=models.IntegerField(default=0, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ['id']



class Favorites(models.Model):
    platillo=models.ForeignKey(RecipesModel,on_delete=models.CASCADE)
    ingredientes=models.ForeignKey(Ingredients, on_delete=models.CASCADE)

    def __str__(self):
        return f"favorito-> {self.platillo}"
    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
        ordering = ['id']
        


