from django.db import models

# Create your models here.
class Input(models.Model):
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return '<{}> {}'.format(self.pk, self.name)

    # def get_absolute_url(self):
    #     return reverse('map:', args=[self.pk])
        