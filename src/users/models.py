from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class user(models.Model):
    
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")
    genderChoices = [('M', 'male'), 
                     ('F', 'female'),
                     ('O', 'other')]
    birthDateRegex = RegexValidator(regex=r'^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$', message="Must be in format YYYY-MM-DD. Must be in the past")
    
    first_name = models.CharField( max_length=15)
    last_name = models.CharField(max_length=15)
    country_code = models.CharField(max_length=3)
    phone_number = models.CharField(validators=[phoneRegex], max_length=17, unique=True)
    gender = models.CharField(max_length=6, choices=genderChoices)
    birthdate = models.CharField(validators=[birthDateRegex], max_length=10)
    avatar = models.ImageField(upload_to ='uploads')
    password = models.CharField(max_length=50, default='a')
    email = models.EmailField(blank=True)
    status = models.CharField(blank=True, max_length=15)
