from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

import requests
import json


@csrf_exempt
def user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def create_ticket(request):
    response = json.loads(requests.get("http://localhost:8000/api/list_topic").text)
    if request.method == 'POST':
        API_ENDPOINT = "http://localhost:8000/api/tk_create"
        API_KEY = request.POST['auth_token']
        TITLE = request.POST['title']
        CONTENT = request.POST['content']
        TOPIC = request.POST['topic']
        client = requests.session()
        client.get(API_ENDPOINT)  
        # sets cookie
        if 'csrftoken' in client.cookies:
            # Django 1.6 and up
            csrftoken = client.cookies['csrftoken']
        else:
            # older versions
            csrftoken = client.cookies['csrf']
        
        data = {'title':TITLE,
                'topic':TOPIC,
                'content':CONTENT,
                'auth_token':API_KEY,
                'csrfmiddlewaretoken': csrftoken}
        
        # sending post request and saving response as response object
        r = client.post(API_ENDPOINT, data = data, headers=dict(Referer=API_ENDPOINT))
    return render(request, 'FirstAPI/index.html', {'list_topic': response})
