from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Count
from ...models import Client



from django.http import HttpResponse
from django.db.models import F, Value
from django.db.models.functions import Concat

import csv

jwt = JWTAuthentication()


class UsersCSV(APIView):
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
    def post(self, request, *args, **kwargs):
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
