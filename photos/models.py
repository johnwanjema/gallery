from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def save_category(self):
        self.save()

    @classmethod
    def update_category(cls,id):
        category = cls.objects.update(id=id)
        return category

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=20)

    def save_location(self):
        self.save()

    @classmethod
    def update_location(cls,id):
        location = cls.objects.update(id=id)
        return location

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos')
    description = models.CharField(max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, default='LOCATION')

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()        
        

    @classmethod
    def get_allImages(cls):
        images = cls.objects.all()
        return images  
    

    @classmethod
    def update_image_by_id(cls,id):
        image = cls.objects.update(id=id)
        return image

    
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id=id)
        return image

    @classmethod
    def search_image_by_category(cls,search_term):
        images = cls.objects.filter(category__name__contains = search_term)
        return images

    @classmethod
    def search_image_by_location(cls,search_term):
        images = cls.objects.filter(location__name__contains = search_term)
        return images

    @classmethod
    def filter_by_location(cls):

        
        pass

   
    def __str__(self):
        return self.name




