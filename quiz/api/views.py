from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serilization import *
from .email import *



@api_view(['POST'])
def RegisterAPI(request):
    print(request)
    if request.method =='POST':       
        try:
            serializer=UserSerializer(data=request.data)
            if serializer.is_valid:
                print("a")
                a=send_otp_via_mail(request.data['email'])
                return Response({
                    'status':200,
                    'message':"Registration successfull",
                    'data':a
                })
            return Response({
                'status':500,
                'message':'something went wrong',
                'otp_verified':'True',

            })
        except:
            print("error")