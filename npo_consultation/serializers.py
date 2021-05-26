from rest_framework import serializers

from npo_consultation.models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    def get_answers(self, obj):
        answers = Answer.objects.filter(question=obj)
        return AnswersSerializer(answers, many=True).data


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
