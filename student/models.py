from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse

# Create your models here.

class CustomUser(AbstractUser):
    user_type_data = ((1, "Principal"), (2, 'Staff'), (3, 'Student'))
    user_type = models.CharField(default = 1, choices = user_type_data, max_length = 10)
    email = models.EmailField(unique = True)
    
class Principal(models.Model):
    id = models.AutoField(primary_key = 1)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    def __str__(self):
        return self.admin.first_name

class Staff(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    number = models.BigIntegerField(null = True)
    Temporary_address = models.CharField(max_length = 300)
    gender = models.CharField(max_length = 100, choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    ), default = 'Male')
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.admin.first_name

class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    id_card = models.BigIntegerField(unique=True)
    number = models.BigIntegerField(null = True)
    Temporary_address = models.CharField(max_length = 300)
    street = models.CharField(max_length = 200)
    district = models.CharField(max_length = 50, default = 'Kathmandu')
    profile_pic = models.ImageField(upload_to = "Seller_Profile", blank = True)
    faculty = models.CharField(max_length= 200, default = "Computer Science")
    gender = models.CharField(max_length = 100, choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    ), default = 'Male')
    objects = models.Manager()
    def __str__(self):
        return self.admin.first_name
    
class attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    morning = models.TimeField(null = True)
    evening = models.TimeField(null = True)
    present = models.BooleanField(default= False)
    count = models.IntegerField(default = 0)
    
@receiver(post_save, sender= CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Principal.objects.create(admin = instance)
        if instance.user_type == 2:
            Staff.objects.create(admin = instance)
        if instance.user_type == 3: 
            Student.objects.create(admin = instance)
            
@receiver(post_save, sender=CustomUser)
def _post_save_receiver(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.principal.save()
    if instance.user_type == 2:
        instance.staff.save()
    if instance.user_type == 3:
        instance.student.save()
