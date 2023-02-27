from rest_framework import generics
from .models import Token
from .serializers import TokenSerializer


class TokenList(generics.ListCreateAPIView):
    queryset= Token.objects.all()
    serializer_class= TokenSerializer


