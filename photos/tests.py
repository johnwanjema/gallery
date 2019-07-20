from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.

class LocationTestClass(TestCase):
    '''
    test for location
    '''
    # Set up method
    def setUp(self):
        self.Nairobi= Location(name = 'Nairobi')
    def test_instance(self):
        self.assertTrue(isinstance(self.Nairobi,Location))

    def test_save_method(self):
        self.Nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)



class CategoryTestClass(TestCase):
    '''
    test for Category
    '''
    # Set up method
    def setUp(self):
        self.Camera= Category(name = 'Camera')
    def test_instance(self):
        self.assertTrue(isinstance(self.Camera,Category))

    def test_save_method(self):
        self.Camera.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)




