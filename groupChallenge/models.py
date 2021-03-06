from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


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
    SUNDAY = 'SUN'
    MONDAY = 'MON'
    TUESDAY = 'TUE'
    WEDNESDAY = 'WED'
    THURSDAY = 'THU'
    FRIDAY = 'FRI'
    SATURDAY = 'SAT'
    DAYS = (
        (SUNDAY, 'SUN'),
        (MONDAY, 'MON'),
        (TUESDAY, 'TUE'),
        (WEDNESDAY, 'WED'),
        (THURSDAY, 'THU'),
        (FRIDAY, 'FRI'),
        (SATURDAY, 'SAT'),
    )
    HEALTH = 'H'
    SPORT = 'S'
    LIFESTYLE = 'L'
    CATEGORIES = (
        (HEALTH, 'H'),
        (SPORT, 'S'),
        (LIFESTYLE, 'L'),
    )
    title = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(max_length=1024, blank=True)
    like_number = models.IntegerField(default=0, blank=True)
    days = ArrayField(
        models.CharField(max_length=3, choices=DAYS, null=False, blank=False)
    )
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    progress_type = models.CharField(max_length=2, choices=PROGRESS_TYPE, null=False, blank=False)
    icon = models.ImageField(upload_to='files/challenge_icon', blank=True)
    private_public_type = models.CharField(max_length=2, choices=PRIVACY_TYPE, null=False, blank=False)
    categories = models.CharField(max_length=20, choices=CATEGORIES, null=True, blank=True)
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.SET_NULL, null=True, blank=False)
    users = models.ManyToManyField(User, related_name='users', through='UserChallengeProgress', null=False, blank=False)
    password = models.CharField(max_length=128, null=True, blank=True, default=None)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['like_number']


class UserChallengeProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, null=False, blank=False)
    percent_progress = models.ForeignKey('PercentProgress', on_delete=models.CASCADE, null=True, blank=True)
    boolean_progress = models.ForeignKey('BooleanProgress', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username + ' | ' + self.challenge.title


class PercentProgress(models.Model):
    time = models.DateField(null=False, blank=False)
    percent = models.IntegerField(null=False, blank=False, default=0)
    user_challenge_progress = GenericRelation(UserChallengeProgress)

    def __str__(self):
        return 'Time: %s | Percent: %s' % (self.time, self.percent)


class BooleanProgress(models.Model):
    time = models.DateField(null=False, blank=False)
    bool_progress = models.BooleanField(null=False, blank=False, default=False)
    user_challenge_progress = GenericRelation(UserChallengeProgress)

    def __str__(self):
        return 'Time: %s | Done: %s' % (self.time, self.bool_progress)


class Feedback(models.Model):
    title = models.CharField(max_length=128, null=True, blank=True)
    content = models.TextField(max_length=1024, null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.title
