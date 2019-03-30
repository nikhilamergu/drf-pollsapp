from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Track, Question, Choice, UserChoice


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'track_text')


class QuesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'track')


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice_text', 'votes')


class UserChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChoice
        fields = ('id', 'question', 'choice', 'is_correct')


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    @action(detail=True, methods=['get'])
    def questions(self, request, pk=None):
        track_questions = Question.objects.filter(track_id=pk)
        page = self.paginate_queryset(track_questions)
        if page is not None:
            serializer = QuesSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = QuesSerializer(track_questions, many=True)
        return Response(serializer.data)


class QuesViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuesSerializer

    @action(detail=True, methods=['get'])
    def correct_answers(self, request, pk=None):
        correct_answers_count = UserChoice.objects.filter(question_id=pk, is_correct=True).count()
        return Response({'count': correct_answers_count, 'question': self.get_object().question_text})

    @action(detail=True, methods=['get'])
    def wrong_answers(self, request, pk=None):
        wrong_answers_count = UserChoice.objects.filter(question_id=pk, is_correct=False).count()
        return Response({'count': wrong_answers_count, 'question': self.get_object().question_text})


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class UserChoiceViewSet(viewsets.ModelViewSet):
    queryset = UserChoice.objects.all()
    serializer_class = UserChoiceSerializer
