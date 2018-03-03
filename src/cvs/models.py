from django.db import models
from django_countries.fields import CountryField

class Skill(models.Model):

   name = models.CharField(max_length=50)
   description = models.TextField(blank=True, null=True)

   def __str__(self):
       """
       Devuelve la representación de un objeto como una string
       """
       return self.name

class Experience(models.Model):

   title = models.CharField(max_length=150)
   summary = models.TextField()
   company = models.CharField(max_length=250)
   from_date = models.DateField()
   to_date = models.DateField()

   created_at = models.DateTimeField(auto_now_add=True) # set date when object is created
   modified_at = models.DateTimeField(auto_now=True)  # saves the date when the object is updated

   def __str__(self):
       """
       Devuelve la representación de un objeto como una string
       """
       return self.title

class Curriculum(models.Model):

   title = models.CharField(max_length=150)
   description = models.TextField()
   canonical = models.URLField(blank=True)

   languages = CountryField(multiple=True)
   nationality = CountryField(blank=True)

   created_at = models.DateTimeField(auto_now_add=True) # set date when object is created
   modified_at = models.DateTimeField(auto_now=True)  # saves the date when the object is updated

   def __str__(self):
       """
       Devuelve la representación de un objeto como una string
       """
       return self.title
