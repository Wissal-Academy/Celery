from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Employe
from .tasks import processing_data


@receiver(post_save, sender=Employe)
def get_employee_data(sender, instance, created, **kwargs):
    if created:
        processing_data.delay(instance.id)
