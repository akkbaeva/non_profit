
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from npo_consultation.models import Question
from npo_consultation.serializers import QuestionSerializer


class QuestionAPIView(APIView):
    allow_methods = ['GET', 'POST']
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        question = Question.objects.all()
        return Response(data=self.serializer_class(question, many=True).data)

    def post(self, request, *args, **kwargs):
        text = request.data.get('text')
        question = Question.objects.create(text=text)
        question.save()
        return Response(data=self.serializer_class(question).data,
                        status=status.HTTP_201_CREATED)
