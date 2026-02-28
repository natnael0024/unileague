from rest_framework import generics
from .serializers import RegisterSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer
from django.utils.timezone import now
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

            user = serializer.validated_data["user"]
            tokens = serializer.create_tokens(user)

            user.last_login = now()
            user.save(update_fields=["last_login"])

            return Response({
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "role": user.role,
                    "university": user.university.name if user.university else None,
                    "department": user.department.name if user.department else None,
                    "year": user.year,
                },
                "tokens": tokens
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

