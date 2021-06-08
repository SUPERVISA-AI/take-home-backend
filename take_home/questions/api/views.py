from django.contrib.auth import get_user_model
# from rest_framework import status
# from rest_framework.decorators import action
# from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework import viewsets

from .serializers import AnswerSerializer, QuestionSerializer, ResponseSerializer, ResponseWriteSerializer, \
    QuestionCategorySerializer
from take_home.questions.models import Answer, Question, Response, QuestionCategory

User = get_user_model()


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get_queryset(self, *args, **kwargs):
        queryset = Question.objects.all()
        category = self.request.query_params.get("category")
        if category is not None:
            queryset = queryset.filter(question_category=category)
        return queryset


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(response__user=self.request.user)


class ResponseViewSet(viewsets.ModelViewSet):
    serializer_class = ResponseSerializer
    queryset = Response.objects.all()

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ResponseWriteSerializer

        return ResponseSerializer


class QuestionCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionCategorySerializer
    queryset = QuestionCategory.objects.all()
