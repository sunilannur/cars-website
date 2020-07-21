from django.db import models
import datetime
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from versatileimagefield.fields import VersatileImageField


class Profile(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField()
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, blank=True)
    dob = models.DateField(blank=True, null=True)
    gen_otp = models.IntegerField(blank=True, null=True)
    otp_expire = models.DateTimeField(blank=True, null=True)
    custom_secret = models.CharField(max_length=256, blank=True, null=True)
    retry_otp_count = models.IntegerField(default=0, blank=True, null=True)
    profile_pic = models.FileField(upload_to='users_profile_pic/', blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    country_code = models.CharField(max_length=30, null=True, blank=True)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Maker(models.Model):
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Model(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Transmission(models.Model):
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Cylinder(models.Model):
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Drivetrain(models.Model):
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SellerType(models.Model):
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Fuel(models.Model):
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Body(models.Model):
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CarImages(models.Model):
    images = models.ImageField()


class Car(models.Model):

    def current_year():
        return datetime.date.today().year

    def max_value_current_year(value):
        return MaxValueValidator(datetime.date.today().year)(value)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    detail = models.TextField()
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=30, decimal_places=3)
    mileage = models.IntegerField()
    body_style = models.ForeignKey(Body, on_delete=models.SET_NULL, null=True)
    year = models.PositiveIntegerField(default=current_year(),
                                       validators=[MinValueValidator(1984), max_value_current_year])
    transmission = models.ForeignKey(Transmission, on_delete=models.SET_NULL, null=True)
    exterior_color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, related_name="exterior_color")
    interior_color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, related_name="interior_color")
    drivetrain = models.ForeignKey(Drivetrain, on_delete=models.SET_NULL, null=True)
    cylinder_count = models.ForeignKey(Cylinder, on_delete=models.SET_NULL, null=True)
    seller_type = models.ForeignKey(SellerType, on_delete=models.SET_NULL, null=True)
    fuel = models.ForeignKey(Fuel, on_delete=models.SET_NULL, null=True)
    phone = PhoneNumberField()
    images = models.ManyToManyField("website.CarImages", blank=True)
    country_code = models.CharField(max_length=30, null=True, blank=True)
    viewed = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class AdViews(models.Model):
    user_ip = models.GenericIPAddressField(null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ad_id = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
