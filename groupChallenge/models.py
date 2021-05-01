from django.db import models
from datetime import datetime


class User(models.Model):
    user_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    avatar = models.FileField(upload_to='files/user_avatar')
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()


class Challenge(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    like_number = models.IntegerField()
    repetition = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    progress_type = models.CharField(max_length=64)
    icon = models.FileField(upload_to='files/challenge_icon')
    private_public_type = models.CharField(max_length=64)
    category = models.OneToOneField('Category', on_delete=models.CASCADE)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()


class UserChallengeProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    percent_progress = models.ForeignKey('PercentProgress', on_delete=models.CASCADE)
    boolean_progress = models.ForeignKey('BooleanProgress', on_delete=models.CASCADE)


class PercentProgress(models.Model):
    time = models.DateTimeField()
    percent = models.IntegerField()


class BooleanProgress(models.Model):
    time = models.DateTimeField()
    bool_progress = models.BooleanField()


class Category(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()


class Feedback(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=1024)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
