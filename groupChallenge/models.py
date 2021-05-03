from django.db import models
from datetime import datetime


class User(models.Model):
    user_name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    email = models.CharField(max_length=64, null=False, blank=False, unique=True)
    password = models.CharField(max_length=64, null=False, blank=False)
    avatar = models.FileField(upload_to='files/user_avatar')
    updated_at = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=False, default=datetime.now)

    def __str__(self):
        return self.user_name


class Challenge(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    description = models.CharField(max_length=1024)
    like_number = models.IntegerField()
    repetition = models.IntegerField(null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    progress_type = models.CharField(max_length=64, null=False, blank=False)
    icon = models.FileField(upload_to='files/challenge_icon')
    private_public_type = models.CharField(max_length=64, null=False, blank=False)
    category = models.ManyToManyField('Category', through='ChallengeCategory', blank=False)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.SET_NULL, null=True, blank=False)
    users = models.ManyToManyField(User, related_name='users', through='UserChallengeProgress')
    updated_at = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=False, default=datetime.now)

    def __str__(self):
        return self.title


class UserChallengeProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, null=False, blank=False)
    percent_progress = models.ForeignKey('PercentProgress', on_delete=models.SET_NULL, null=True, blank=False)
    boolean_progress = models.ForeignKey('BooleanProgress', on_delete=models.SET_NULL, null=True, blank=False)


class PercentProgress(models.Model):
    time = models.DateTimeField(null=False, blank=False)
    percent = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.time, self.percent


class BooleanProgress(models.Model):
    time = models.DateTimeField(null=False, blank=False)
    bool_progress = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return self.time, self.bool_progress


class Category(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=1024, null=False, blank=False)
    updated_at = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=False, default=datetime.now)

    def __str__(self):
        return self.title


class ChallengeCategory(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.challenge, self.category


class Feedback(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=1024, null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.title
