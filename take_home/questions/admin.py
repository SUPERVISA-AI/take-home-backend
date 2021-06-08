from django.contrib import admin
from .models import Answer, Question, QuestionCategory, Response

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(QuestionCategory)
admin.site.register(Response)
