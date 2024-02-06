from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import datetime
from accounts.models import User, Profile
from blog.models import Post, Category


category_list = [
    'IT',
    'Machine Learning',
    'Deep Learning',
    'Computer Vision',
    'Computer Science',
    'Devops',
    'Data Engineering',
]

class Command(BaseCommand):
    help = "inserting dummy data"
    
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()
        

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(), password='test@123456')
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=5)
        profile.save()
        
        # Create category profile
        for category in category_list:
            Category.objects.get_or_create(name=category)
            
        # Create posts
        for _ in range(10):
            Post.objects.create(
                author = profile,
                title = self.fake.paragraph(nb_sentences=1),
                content = self.fake.paragraph(nb_sentences=10),
                status = random.choice([True, False]),
                category = Category.objects.get(name=random.choice(category_list)),
                published_date = datetime.now(),
            )