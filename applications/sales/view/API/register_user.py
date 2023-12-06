from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Count

from django.contrib.auth.models import User
from ...models import Client

from ...serializers import UserSerializer


from django.http import HttpResponse
from django.db.models import F, Value
from django.db.models.functions import Concat

import re, csv

regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")

jwt = JWTAuthentication()


def isValidEmail(email):
    if re.fullmatch(regex, email):
        return True
    else:
        False


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

    def get(self, request, *args, **kwargs):
        # if not jwt.authenticate(request=request):
        #     return Response(
        #         {"message": "Unauthorized process"}, status=status.HTTP_401_UNAUTHORIZED
        #     )
        try:
            clients = Client.objects.values(
                Company_name=F("bill__company_name"),
                Documento=F("document"),
            ).annotate(
                nombre_completo=Concat("first_name", Value(" "), "last_name"),
                Numero_de_Facturas=Count("bill"),
            )
            response = HttpResponse(
                content_type="text/csv",
                headers={
                    "Content-Disposition": 'attachment; filename="somefilename.csv"'
                },
            )
            writer = csv.DictWriter(response, fieldnames=list(clients)[0].keys())
            writer.writeheader()
            for item in clients:
                writer.writerow(item)
            return response
        except Exception as e:
            print(e)
            return Response(
                {"status": "ERROR", "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
