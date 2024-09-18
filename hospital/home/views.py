from home.models import *
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response



class RegistrationApiView(APIView):
    def post(self, request, format = None):

        if not request.data.get("first_name"):
            return Response({"message": "Please enter first_name", "status":status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        
        if not request.data.get("last_name"):
            return Response({"message": "Please enter last_name", "status":status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        
        if not request.data.get("email"):
            return Response({"message": "Please enter email", "status":status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        
        if not request.data.get("phone_number"):
            return Response({"message": "Please enter phone_number", "status":status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        
        if not request.data.get("password"):
            return Response({"message": "Please enter password", "status":status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        
        if not request.data.get("confirm_password"):
            return Response({"message": "Please enter confirm_password", "status":status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        
        if request.data.get("password") != request.data.get("confirm_password"):
            return Response({"message": "Both passwords are no matching", "status":status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
        try:

            if not User.objects.filer(email = request.data.get("email")).exists():
                user = User.objects.create(
                    first_name = request.data.get("first_name"),
                    last_name = request.data.get("last_name"),
                    email = request.data.get("email"),
                    phone_number = request.data.get("phone_number"),
                    password = request.data.get("password"),
                    confirm_password = request.data.get("confirm_password"),
                    )
            return Response({"msg":"User registered successfully", "status":status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"msg":"User registered with this email, use different email", "status":status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)

