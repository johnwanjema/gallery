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

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new locatio and saving it
        self.Nairobi= Location(name = 'Nairobi')
        self.Nairobi.save_location()

        # Creating a new category and saving it
        self.Camera= Category(name = 'Camera')
        self.Camera.save_category()

        self.new_image= Image(name = 'Test image',photo = '1.jpg',description = 'test',category = self.Camera, location = self.Nairobi)
        self.new_image.save_image()

    

    def test_save_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.new_image.delete_image
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

   

    

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()






