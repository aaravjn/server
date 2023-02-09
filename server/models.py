from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=500, null=False)
    metamask_id = models.TextField(max_length=500, null=False)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Lottery(models.Model):
    start = models.DateField(primary_key=True)
    winner = models.ManyToManyField(User, blank=True, related_name='won_lotteries')
    participants = models.ManyToManyField(User, blank=True, related_name='registered_lotteries')
    end = models.DateField()
    transaction_completed = models.BooleanField(default=False)

    def get_current_lottery(self):
        return self.objects.all().last()
