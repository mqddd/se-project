from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, null=False, blank=False)
    password = models.CharField(max_length=64, null=False, blank=False)
    avatar = models.FileField(upload_to='files/user_avatar')


class Challenge(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    category = models.OneToOneField('Category')
    owner = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=1024)


class Feedback(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    content = models.CharField(max_length=1024, null=False, blank=False)
    owner = models.OneToOneField(User, null=False, blank=False)


