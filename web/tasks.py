from celery import shared_task
import time
import requests

from .models import Employe


@shared_task
def processing_data(instance_id):
    data = requests.get(
            'https://678657a8f80b78923aa671f9.mockapi.io/api/v1/comments'
            )
    # Get object
    employe_obj = Employe.objects.get(id=instance_id)
    print('before')
    print("----------------------------")
    employe_obj.data = data.text()
    employe_obj.status = 'FINISHED'
    employe_obj.save()
    time.sleep(15)
    print('After')
    print("----------------------------")
