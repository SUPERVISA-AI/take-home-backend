from django.contrib import admin

from .models import Answer, Question, QuestionList, Response


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0
    show_change_link = True


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(QuestionList)
