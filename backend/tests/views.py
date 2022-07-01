from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

from .services import *


class Languages(ListCreateAPIView):
    """ Api for all languages and frameworks. """

    queryset = get_all_objects(Test)
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticated]


class LanguagesChoices(Languages):
    """ Api for user choices: level and type """

    def get_queryset(self):
        user_date = self.request.query_params
        return Test.objects.filter(level=user_date['level'], type_of=user_date['type_of'])

class QuestionView(ListAPIView):
    queryset = get_all_objects(Question)
    serializer_class = QuestionSerializer
    lookup_field = 'test__id'
