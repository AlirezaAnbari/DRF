from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models.users import User
from accounts.models.profiles import Profile


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    """
    Signal for post creating a user which activates when a user being created ONLY
    """
        # Use this condition because if you don't use that,
        # when you change some information it create another profile for you.
    if created:                                  
        Profile.objects.create(user=instance)