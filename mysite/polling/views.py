import json
from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse
from django.core import serializers
# Create your views here.

JSONSerializer = serializers.get_serializer('json')



def users_list(request):
    users = User.objects.get()
    jsonSerializer = JSONSerializer()
    jsonSerializer.serialize([users])
    data = jsonSerializer.getvalue()
    return JsonResponse(data,safe=False)