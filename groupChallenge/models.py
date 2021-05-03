from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType


class User(models.Model):
    user_name = models.CharField(max_length=64, null=False, blank=False, unique=True)
    email = models.CharField(max_length=64, null=False, blank=False, unique=True)
    password = models.CharField(max_length=64, null=False, blank=False)
    avatar = models.FileField(upload_to='files/user_avatar')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_name)


class Challenge(models.Model):
    PUBLIC = 'PU'
    PRIVATE = 'PR'
    PRIVACY_TYPE = (
        (PUBLIC, 'PUBLIC'),
        (PRIVATE, 'PRIVATE'),
    )
    PERCENT = 'PE'
    BOOLEAN = 'BO'
    PROGRESS_TYPE = (
        (PERCENT, 'PERCENT'),
        (BOOLEAN, 'BOOLEAN'),
    )
    title = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(max_length=1024)
    like_number = models.IntegerField()
    repetition = models.IntegerField(null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    progress_type = models.CharField(max_length=2, choices=PROGRESS_TYPE, null=False, blank=False)
    icon = models.FileField(upload_to='files/challenge_icon')
    private_public_type = models.CharField(max_length=2, choices=PRIVACY_TYPE, null=False, blank=False)
    category = models.ManyToManyField('Category', through='ChallengeCategory', blank=False)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.SET_NULL, null=True, blank=False)
    users = models.ManyToManyField(User, related_name='users', through='UserChallengeProgress')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class UserChallengeProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, null=False, blank=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class PercentProgress(models.Model):
    time = models.DateTimeField(null=False, blank=False)
    percent = models.IntegerField(null=False, blank=False, default=0)
    user_challenge_progress = GenericRelation(UserChallengeProgress)

    def __str__(self):
        return str(self.time) + ' ' + str(self.percent)


class BooleanProgress(models.Model):
    time = models.DateTimeField(null=False, blank=False)
    bool_progress = models.BooleanField(null=False, blank=False, default=False)
    user_challenge_progress = GenericRelation(UserChallengeProgress)

    def __str__(self):
        return str(self.time) + ' ' + str(self.bool_progress)


class Category(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(max_length=1024, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ChallengeCategory(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return str(self.challenge) + ' ' + str(self.category)


class Feedback(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=1024, null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.title
