from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from ...serializers import UserSerializer
from django.contrib.auth.models import User

from ...utils.helpers import isValidEmail

jwt = JWTAuthentication()


class UserRegister(APIView):
    def post(self, request, *args, **kwargs):
        if not jwt.authenticate(request=request):
            return Response(
                {"message": "Unauthorized process"}, status=status.HTTP_401_UNAUTHORIZED
            )

        serializador = UserSerializer(data=request.data)
        if not serializador.is_valid():
            return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializador.validated_data

        try:
            if not isValidEmail(data["email"]):
                raise Exception("Email not valid")

            username = data["email"].split("@")[0]
            User.objects.create_user(
                username=username, password=data["password"], email=data["email"]
            )
        except Exception as e:
            return Response(
                {"status": "ERROR", "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"status": "SUCCESS", "message": "User created succesfully"},
            status=status.HTTP_200_OK,
        )
