from django.contrib import admin
from .models import Answer, Question, QuestionList, Response

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(QuestionList)
admin.site.register(Response)
