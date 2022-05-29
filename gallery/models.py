from unittest import mock
from django.db import models

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length=80, unique= True)

    class Meta:
        ordering = ["location"]
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()
        
    
    def delete_location(self):
        self.delete()

class Category(models.Model):
    category_name = models.CharField(max_length=80, unique= True)

    class Meta:
        ordering = ["category"]
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()
        
    
    def delete_category(self):
        self.delete()

class Image(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    photo = models.ImageField(upload_to = 'photos/')
    category = models.ForeignKey(Category, related_name='category', on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, related_name='location', on_delete=models.DO_NOTHING)


    def save_image(self):
        self.save()
    
    
    def delete_image(self):
        self.delete()

    def summary(self):
        return self.description[:100]+" ......"
    
    def pub_date(self):
        return self.pub_date.strftime('%b %e %Y')
    
    def update_image(self):
        pass
        
    def get_image_by_id(cls):
        images = cls.objects.get(pk=id)
        return images
    
    def search_image(category):
        pass
    
    def filter_by_location(location):
        pass

   
    