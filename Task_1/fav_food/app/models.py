from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    sex = models.CharField(max_length=25, null=False, blank=False)
    d_o_b = models.DateField(null=False, blank=False)
    favourite_food = models.CharField(max_length=50, null=False, blank=False)

    class Meta :
        db_table = 'favourite_food'

    def __str__(self):
        return self.name
