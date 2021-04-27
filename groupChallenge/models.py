from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=64, null=False, blank=False)
    email = models.CharField(max_length=64, null=False, blank=False)
    password = models.CharField(max_length=64, null=False, blank=False)
    avatar = models.FileField(upload_to='files/user_avatar')
    updated_at = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=False)


class Challenge(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    description = models.CharField(max_length=1024, null=False, blank=False)
    like_number = models.IntegerField()
    repetition = models.IntegerField(null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    type = models.CharField(max_length=64, null=False, blank=False)
    icon = models.FileField(upload_to='files/challenge_icon')
    category = models.OneToOneField('Category', on_delete=models.CASCADE)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=False)


class UserChallengeProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    percent_progress = models.ForeignKey('Progress', on_delete=models.CASCADE)
    boolean_progress = models.ForeignKey('Progress', on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=1024)
    updated_at = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=False)


class Feedback(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    content = models.CharField(max_length=1024, null=False, blank=False)
    owner = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
