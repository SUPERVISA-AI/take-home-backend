from django.contrib import admin

from .models import Answer, Question, QuestionList, Response


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0
    show_change_link = True
    readonly_fields = ("question", "text")


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(QuestionList)
