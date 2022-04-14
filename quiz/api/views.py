from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serilization import *
from .email import *

# class RegisterAPI(APIView):
#     def post(self,request):
#         try:
#             data=request.data
#             serializer=UserSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(data)
#             return serializer.errors
#         except Exception as e:
#             print(e)



# class RegisterAPI(APIView):
    
#     def post(self,request):
#         try:
#             serializer=UserSerializer(data=request.data)
#             if request.method=='POST':
#                 if serializer.is_valid():
#                     print(serializer.data)
#                     print(serializer.data['email'])
#                     send_otp_via_mail(serializer.data['email'])
#                     print("hi")
                    
#                     return Response({
#                         'status':200,
#                         'message':"Registration successfull",
#                         'data':serializer.data
#                     })
                
#                 return Response({
#                     'status':500,
#                     'message':'something went wrong',
#                     'data':serializer.errors
#                 })
#         except Exception as e:
#             print(e)


@api_view(['POST'])
def RegisterAPI(request):
    if request.method =='POST':       
        try:
            serializer=UserSerializer(data=request.data)
            if serializer.is_valid:
                a=send_otp_via_mail(request.data['email'])
                print(a)
                return Response({
                    'status':200,
                    'message':"Registration successfull",
                    'otp_verified':'True',
                    'data':serializer.data
                })
            print(a)
            return Response({
                'status':500,
                'message':'something went wrong',
                'otp_verified':'True',
                'data':serializer.error
            })
        except:
            print("error")