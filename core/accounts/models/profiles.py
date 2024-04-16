from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .users import User


class Profile(models.Model):
    """
    Profile class for each user which is being created to hold the information
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) 
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    """
    Signal for post creating a user which activates when a user being created ONLY
    """
        # Use this condition because if you don't use that,
        # when you change some information it create another profile for you.
    if created:                                  
        Profile.objects.create(user=instance)
