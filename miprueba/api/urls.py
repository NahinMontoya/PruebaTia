from django.urls import path
from .views import TokenList

urlpatterns =[
    path('token/',TokenList.as_view(), name ='token_list'),
]