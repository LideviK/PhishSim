from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.mail import send_mail

class TestRoute(APIView):
    
    def post(self, request):
        send_mail('P', 'Here is the message.', 'from@example.com', ['hftest2@sharklasers.com'], fail_silently=False)
        return Response("Test route...")