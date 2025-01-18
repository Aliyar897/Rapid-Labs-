from rest_framework_simplejwt.views import TokenObtainPairView # type: ignore
from user.serializers import MyTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUser, IsManagerUser, IsRegularUser
from .models import CustomUser, Team
from rest_framework.exceptions import PermissionDenied, NotAuthenticated

from rest_framework import status
from .serializers import TeamSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class AdminView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        # List all users
        users = CustomUser.objects.all()
        return Response({'users': [user.username for user in users]})


class ManagerView(APIView):
    permission_classes = [IsAuthenticated, IsManagerUser]

    def get(self, request):
        if not request.user.is_authenticated:
            raise NotAuthenticated("Authentication credentials were not provided.")

        try:
            team = Team.objects.get(manager=request.user)
            members = team.members.all()
            return Response({'team_members': [user.username for user in members]})
        except Team.DoesNotExist:
            raise PermissionDenied("You do not have a team assigned.")

    def put(self, request):
        if not request.user.is_authenticated:
            raise NotAuthenticated("Authentication credentials were not provided.")

        try:
            team = Team.objects.get(manager=request.user)
            # Logic to update team members
            return Response({'message': 'Team updated'})
        except Team.DoesNotExist:
            raise PermissionDenied("You do not have a team assigned.")


class UserView(APIView):
    permission_classes = [IsAuthenticated, IsRegularUser]

    def get(self, request):
        # View own profile
        return Response({'username': request.user.username})

    def put(self, request):
        # Update own profile
        return Response({'message': 'Update profile'})

class ManagerView(APIView):
    permission_classes = [IsAuthenticated, IsManagerUser]

    def get(self, request):
        # List users assigned to the manager's team
        try:
            team = Team.objects.get(manager=request.user)
            members = team.members.all()
            return Response({'team_members': [user.username for user in members]})
        except Team.DoesNotExist:
            raise PermissionDenied("You do not have a team assigned.")

    def put(self, request):
        # Update users assigned to the manager's team
        try:
            team = Team.objects.get(manager=request.user)
            # Logic to update team members
            return Response({'message': 'Team updated'})
        except Team.DoesNotExist:
            raise PermissionDenied("You do not have a team assigned.")

class CreateTeamView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
