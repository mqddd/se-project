from django.contrib import admin

from .models import *


admin.site.register(Challenge)
admin.site.register(Feedback)
admin.site.register(UserChallengeProgress)
admin.site.register(PercentProgress)
admin.site.register(BooleanProgress)

