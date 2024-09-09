from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def assign_default_group(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        default_group = Group.objects.get(name='Empleado_L1')
        instance.groups.add(default_group)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(pre_save, sender=User)
def lowercase_username(sender, instance, **kwargs):
    if instance.username:
        instance.username = instance.username.lower()