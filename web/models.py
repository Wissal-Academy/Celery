from django.db import models


class Employe(models.Model):
    STATUS = (
        ('PROGRES', 'In Progress'),
        ('FINISHED', 'Completed')
    )

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    age = models.PositiveIntegerField(default=0)

    data = models.TextField(blank=True)
    status = models.CharField(
        max_length=200,
        choices=STATUS,
        default='PROGRESS'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
