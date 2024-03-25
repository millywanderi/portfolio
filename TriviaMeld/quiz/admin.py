from django.contrib import admin
from .models import Quiz, Question, Option

# Register your models here.
class QuizAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "description", "quiz_id")

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Option)
