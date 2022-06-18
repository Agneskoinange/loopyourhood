from django.test import TestCase
from .models import NeighbourHood,Business
from django.contrib.auth.models import User
# Create your tests here.
class NeighbourHoodTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new location and saving it
        self.new_user=User(username='denno',email='a@gmail.com',password='qwerty1234')
        self.new_user.save()
        
        self.new_hood= NeighbourHood(hood_admin=self.new_user,hood_name='Wazazi',hood_location='Chuom')
        self.new_hood.save()



    # Tear Down method
    def tearDown(self):
        NeighbourHood.objects.all().delete()
        User.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_hood,NeighbourHood))    

    # Testing Save Method
    def test_create_neighbourhood_method(self):
        self.new_hood1= NeighbourHood(hood_admin=self.new_user,hood_name='Wazazi',hood_location='Chuom')
        self.new_hood1.create_neighbourhood()
        hoods = NeighbourHood.objects.all()
        self.assertTrue(len(hoods) == 2)  



    # Testing delete method
    def test_delete_neighbourhood(self):
        NeighbourHood.delete_neighbourhood(self.new_hood.id)
        hoods = NeighbourHood.get_all_neighbourhoods()
        self.assertTrue(len(hoods) == 0)     

    # Testing get all NeighbourHoods Method
    def test_get_all_neighbourhoods_method(self):
        hoods = NeighbourHood.get_all_neighbourhoods()
        self.assertTrue(len(hoods) == 1) 


    # Testing find NeighbourHood Method
    def test_find_neighbourhood_method(self):
        hood = NeighbourHood.find_neighbourhood(self.new_hood.id)
        self.assertEqual(hood.id,self.new_hood.id)   





class BusinessTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new location and saving it
        self.new_user=User(username='denno',email='a@gmail.com',password='qwerty1234')
        self.new_user.save()
        
        self.new_hood= NeighbourHood(hood_admin=self.new_user,hood_name='Wazazi',hood_location='Chuom')
        self.new_hood.save()

        self.new_bs=Business(user=self.new_user,neighbourhood=self.new_hood,bs_name='Watchman',bs_description='Watchman',bs_email='a@gmail.com')
        self.new_bs.save()


    # Tear Down method
    def tearDown(self):
        Business.objects.all().delete()
        NeighbourHood.objects.all().delete()
        User.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_bs,Business))    

    # Testing Save Method
    def test_create_business_method(self):
        self.new_bs1= Business(user=self.new_user,neighbourhood=self.new_hood,bs_name='Watchman',bs_description='Watchman',bs_email='a@gmail.com')
        self.new_bs1.create_business()
        bss = Business.objects.all()
        self.assertTrue(len(bss) == 2)  



    # Testing delete method
    def test_delete_business(self):
        self.new_bs.delete_business()
        bss = Business.objects.all()
        self.assertTrue(len(bss) == 0)     

    # Testing get all Business By Hood Method
    def test_get_all_bs_by_hood_method(self):
        self.new_hood1= NeighbourHood(hood_admin=self.new_user,hood_name='Wazazi',hood_location='Chuom')
        self.new_hood1.save()
        self.new_bs1= Business(user=self.new_user,neighbourhood=self.new_hood1,bs_name='Watchman',bs_description='Watchman',bs_email='a@gmail.com')
        self.new_bs1.create_business()
        bss = Business.get_all_bs_by_hood(self.new_hood1.id)
        self.assertTrue(len(bss) == 1) 


    # Testing find Business Method
    def test_find_business_method(self):
        bs = Business.find_business(self.new_bs.id)
        self.assertEqual(bs.id,self.new_bs.id)   

    # Testing search business by name method
    def test_search_project(self):
        self.new_hood1= NeighbourHood(hood_admin=self.new_user,hood_name='Wazazi',hood_location='Chuom')
        self.new_hood1.save()
        self.new_bs1= Business(user=self.new_user,neighbourhood=self.new_hood1,bs_name='Watchman',bs_description='Watchman',bs_email='a@gmail.com')
        self.new_bs1.create_business()
        self.new_bs2= Business(user=self.new_user,neighbourhood=self.new_hood1,bs_name='Shoe repair',bs_description='Watchman',bs_email='a@gmail.com')
        self.new_bs2.create_business()
        bss=Business.search_business('wat',self.new_hood.id)
        bsss=Business.search_business('Sho',self.new_hood.id)
        self.assertFalse(len(bsss) > 0)  
        self.assertTrue(len(bss) > 0) 

