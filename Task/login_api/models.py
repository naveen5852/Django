from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    emp_id = models.CharField(primary_key=True, max_length=15)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=False, blank=False)
    d_o_b = models.DateField(null=False, blank=False)
    location = models.CharField(max_length=50, null=False, blank=False)
    project = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.name


class UserAssetDetail(models.Model):
    emp_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    lap_model = models.CharField(max_length=50, null=False, blank=False)
    lap_number = models.CharField(max_length=50, null=False, blank=False)
    lap_SNo = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = "asset_detail"

    def __str__(self):
        return self.name


class UserFamilyDetail(models.Model):
    emp_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    father = models.CharField(max_length=50, null=False, blank=False)
    mother = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = "family_detail"