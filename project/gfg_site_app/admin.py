from django.contrib import admin
from .models import StudyModel # StudyModel is a class in models.py
from .models import *
from .models import QuizAttempt, AnswerRecord
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# The models are rendered on views.py
# A model is a Python class that defines the structure of a database table
# each model on models.py is registered below:


# Models for questions and answers
class AnswerAdmin(admin.StackedInline):
    model = Answer # By default Django will offer 3 quiz answer options

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

# Models for quiz attempt records
class QuizAttemptInline(admin.TabularInline):
    model = QuizAttempt
    extra = 0

class CustomUserAdmin(UserAdmin):
    inlines = [QuizAttemptInline]



class AnswerRecordInline(admin.TabularInline):
    model = AnswerRecord
    extra = 0
    readonly_fields = ("question", "is_correct", "seconds_taken")
    can_delete = False


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "gfg", "score", "total", "percent", "timestamp")
    list_filter = ("gfg", "user")
    inlines = [AnswerRecordInline]


admin.site.unregister(User) # removes the default admin interface Django ships with for the User model (the standard username/password/permissions page).
admin.site.register(User, CustomUserAdmin) # re-registers User with your custom admin interface (CustomUserAdmin), which adds the QuizAttemptInline so attempts show up on that page.


# Registering the models so it shows up in /admin
admin.site.register(StudyModel)
admin.site.register(Topic)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
