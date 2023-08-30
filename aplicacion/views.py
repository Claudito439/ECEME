import json
import random

from django.shortcuts import render
from django.views import View
from rest_framework.decorators import api_view

from .models import Pais, Fuerza, Regimiento
from rest_framework import status
from rest_framework.response import Response
from .serializer import *
import requests
from django.http import JsonResponse

COLORS = ["bg-white" ,"bg-yellow-500","bg-pink-500","bg-cyan-400", "bg-red-600"]
@api_view(['GET', 'POST'])
def MenuListView(request):
    if request.method=='GET':
        paises = Pais.objects.all()
        serializers=PaisSerializer(paises,many=True)
        response=serializers.data
        json=[]
        v=0
        for i in response:
            j={}
            j["name"]=i['nombre']
            j["initials"]=i["abreviacion"]
            j["bgColor"]=COLORS[v]
            fuerzas = Fuerza.objects.filter(pais=i["id"])
            f = FuerzaSerializer(fuerzas, many=True)
            fuer=[]
            for y in f.data:
                js={}
                js["name"]=y["nombre"]
                regimientos = Regimiento.objects.filter(fuerza=y["id"])
                regi = RegimientoSerializer(regimientos, many=True)
                reg=[]
                for z in regi.data:
                    u={"name":z["nombre"]}
                    reg.append(u)
                js["regimientos"]=reg
                fuer.append(js)
            j["fuerzas"]=fuer
            json.append(j)
            v=v+1
        return Response(json,status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def BuscarView(request):
    if request.method == 'POST':
        my_string = request.data['cadena']

        # Google API
        google_url = 'https://www.googleapis.com/customsearch/v1'
        google_api_key = 'AIzaSyDAtSRerQJDwGr80DwuocHuzY4IqEWi6Qo'
        google_cx = '361612ba6d9024f03'

        google_results = []

        for start_index in range(1, 21, 10):
            google_params = {
                'q': my_string,
                'cx': google_cx,
                'key': google_api_key,
                'sort': 'date',
                'start': start_index
            }

            google_response = requests.get(google_url, params=google_params)
            google_data = google_response.json()

            if 'items' in google_data:
                for item in google_data['items']:
                    result = {
                        'link': item['link'],
                        'date': item['snippet']
                    }
                    google_results.append(result)  # Agregar aquí para cada resultado


        return Response({
            'resultados_google': google_results
        })