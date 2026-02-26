from rest_framework import generics
from .serializers import RegisterSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer
from django.utils.timezone import now

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        tokens = serializer.create_tokens(user)

        user.last_login = now()
        user.save(update_fields=["last_login"])

        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,
                "university": user.university.id if user.university else None,
                "department": user.department.id if user.department else None,
                "year": user.year,
            },
            "tokens": tokens
        }, status=status.HTTP_200_OK)
