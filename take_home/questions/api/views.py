from rest_framework import response, status, viewsets

from take_home.questions.models import Answer, Question, QuestionList, Response

from .serializers import (
    AnswerSerializer,
    QuestionListSerializer,
    QuestionSerializer,
    ResponseSerializer,
    ResponseWriteSerializer,
)


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get_queryset(self, *args, **kwargs):
        queryset = Question.objects.all()
        question_list = self.request.query_params.get("list")
        if question_list is not None:
            queryset = queryset.filter(question_list=question_list)
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Use a different serializer with more data for the response
        response_data = ResponseSerializer(serializer.instance).data
        return response.Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ResponseWriteSerializer

        return ResponseSerializer


class QuestionListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionListSerializer
    queryset = QuestionList.objects.all()
