from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from info.email import message
from info.models import(
    SubmitApplication,
)
from info.serializers import(
    SubmitApplicationSerializer,
)


class SubmitApplicationView(APIView):
    def post(self, request):
        serializer  = SubmitApplicationSerializer(data=request.data)
        data = serializer.validated_data
        name = data.get('name')
        email = data.get('email')
        message.delay(email)
        SubmitApplication.save

