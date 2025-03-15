from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=51)
    password = models.CharField(max_length=40)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verify = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)


class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    contact = models.CharField(max_length=13)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=20)
    gender = models.CharField(max_length=50)
    current_salary = models.BigIntegerField(null= True)
    expected_salary = models.BigIntegerField(null=True)
    country = models.CharField(max_length=150, null=True)
    highest_education = models.CharField(max_length=150, null=True)
    experience = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=500, null=True)
    profile_pic = models.ImageField(upload_to="app/image/candidate")


class Company(models.Model):
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    logo_pic = models.ImageField(upload_to="app/image/company")
