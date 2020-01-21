from rest_framework import generics

from users.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """ Create a bew user in the system """
    serializer_class = UserSerializer
