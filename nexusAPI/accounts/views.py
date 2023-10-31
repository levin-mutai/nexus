from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from .serializers import UserRegistrationSerializer,StaffRegistrationSerializer,UserListSerializer
from .models import User




# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    "Use this route to register a new user. Four fields must be provided: username, email, customer_name and password"
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class StaffRegistrationView(generics.CreateAPIView):
#     """Used to register new staffs by the shop owner"""
#     permission_classes = [IsAdminUser]

#     def register_staff(self,request,*args, **kwargs):
#         serializer = StaffRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StaffListView(generics.ListAPIView):
#     permission_classes = [IsAdminUser]
#     serializer_class = StaffRegistrationSerializer

#     def get_queryset(self):
#         queryset = User.objects.filter(is_staff=True)
#         return queryset
