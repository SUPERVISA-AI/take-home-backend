from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Response(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="responses")

    def __str__(self):
        return f"{self.id}: {self.user}"


class QuestionList(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class QuestionType(models.TextChoices):
    TEXT = "TEXT", _("Text")
    YES_NO = "YES_NO", _("Yes No")
    NUMBER = "NUMBER", _("Number")
    MULTIPLE_CHOICE = "MC", _("Multiple Choice")


class Question(models.Model):
    text = models.CharField(max_length=255)
    question_list = models.ForeignKey(QuestionList, on_delete=models.CASCADE, related_name="questions")
    question_type = models.CharField(
        max_length=6, choices=QuestionType.choices, default=QuestionType.TEXT,
    )
    choices = models.CharField(max_length=255, null=True, blank=True, help_text=_("Text choices separated by comma"))

    def __str__(self):
        return f"{self.id}: {self.text} - {self.question_type} - {self.question_list}"

    @property
    def choice_list(self):
        if self.question_type == QuestionType.MULTIPLE_CHOICE and self.choices:
            return [choice.strip() for choice in self.choices.split(",")]
        return None


class Answer(models.Model):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name="answers")

    def __str__(self):
        return f"{self.id}: {self.question} - {self.response.id}"
