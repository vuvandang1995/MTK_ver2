from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from api.serializers import *
from user.models import *
from user.forms import *
from user.views import handle_uploaded_file

@csrf_exempt
# Hàm cho phép tạo ticket qua API
def tk_create(request):
    if request.method == 'POST':
        try:
            token = request.POST['auth_token']
            user = Users.objects.get(token=token)
            form = CreateNewTicketForm(request.POST,request.FILES)
            if form.is_valid():
                topicA = Topics.objects.get(id=request.POST['topic'])
                ticket = Tickets()
                ticket.title = form.cleaned_data['title']
                ticket.content = form.cleaned_data['content']
                ticket.sender = user
                ticket.topicid = topicA
                ticket.datestart = timezone.now()
                ticket.dateend = (timezone.now() + timezone.timedelta(days=3))
                if request.FILES.get('attach') is not None:
                    if request.FILES['attach']._size < MAX_UPLOAD_SIZE:
                        ticket.attach = request.FILES['attach']
                        handle_uploaded_file(request.FILES['attach'])
                ticket.save()
        except:
            pass
    return redirect('/')


# hàm cho phép get Topic qua API
def list_topic(request):
    if request.method == 'GET':
        topics = Topics.objects.all()
        serializer = TopicsSerializer(topics, many=True)
        return JsonResponse(serializer.data, safe=False)
