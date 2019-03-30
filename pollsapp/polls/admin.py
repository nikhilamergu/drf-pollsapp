from django.contrib import admin

from .models import Track, Question, Choice, UserChoice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Track)
admin.site.register(UserChoice)
