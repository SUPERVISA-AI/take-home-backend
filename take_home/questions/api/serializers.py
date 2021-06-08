from django.contrib.auth import get_user_model
from rest_framework import serializers

from take_home.questions.models import Question, Answer, Response, QuestionList

User = get_user_model()


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionList
        fields = ["id", "name"]


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ["id", "text", "question_list", "question_type", "choice_list"]


class QuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ["id", "text", "choice_list"]


class AnswerSerializer(serializers.ModelSerializer):
    question = QuestionAnswerSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ["id", "response", "question", "text"]


class AnswerWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ["text", "question"]


class AnswerResponseSerializer(serializers.ModelSerializer):
    question = QuestionAnswerSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ["question", "text"]


class ResponseSerializer(serializers.ModelSerializer):
    answers = AnswerResponseSerializer(many=True)

    class Meta:
        model = Response
        fields = ["id", "user", "answers"]


class ResponseWriteSerializer(serializers.ModelSerializer):
    answers = AnswerWriteSerializer(many=True)

    class Meta:
        model = Response
        fields = ["id", "user", "answers"]
        read_only_fields = ["user"]

    def create(self, validated_data):
        answer_data = validated_data.pop("answers")
        response = Response.objects.create(**validated_data)
        for answer in answer_data:
            Answer.objects.create(response=response, **answer)

        return response
