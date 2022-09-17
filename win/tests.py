from django.test import TestCase
from .models import Profile,Win

# Create your tests here.

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.lewis=Profile(Bio='Lewis Murgor')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.lewis,Profile))

    # Testing Save Method
    def test_save_profile(self):
        self.lewis.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

     # Testing Delete Method
    def test_delete_profile(self):
        self.lewis.save_profile()
        self.lewis.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

class WinTestClass(TestCase):

     # Set up method
    def setUp(self):
        # Creating a new profile and saving it
        self.lewis=Profile(Bio='Lewis Murgor')
        self.lewis.save_profile()

        self.new_win=Win(title='graduation',text='Graduated from moringa school',comments='Beautiful')
        self.new_win.save_win()

    def tearDown(self):
        Profile.objects.all().delete()
        Win.objects.all().delete()

    # Testing  instance
    def test_check_instance_variables(self):
        self.assertEqual(self.new_win.title, 'graduation')
        self.assertEqual(self.new_win.text, 'Graduated from moringa school')
        self.assertEqual(self.new_win.comments, 'Beautiful')

    # Testing Save Method
    def test_save_win(self):
        self.new_win.save_win()
        wins = Win.objects.all()
        self.assertTrue(len(wins) > 0)

    # Testing Delete Method
    def test_delete_win(self):
        self.new_win.save_win()
        self.new_win.delete_win()
        wins = Win.objects.all()
        self.assertTrue(len(wins) == 0)
