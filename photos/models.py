from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def save_category(self):
        self.save()

    def __str__(self):
        return self.name
    

class Location(models.Model):
    name = models.CharField(max_length=20)

    def save_location(self):
        self.save()


    def __str__(self):
        return self.name

    

class Image(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos')
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default='LOCATION')

    def __str__(self):
        return self.name



    

    
    