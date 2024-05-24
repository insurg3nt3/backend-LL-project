from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User
from rest_framework.response import Response

from .serializers import UserSerializer, MenuSerializer, BookingSerializer
from .models import Menu, Booking
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


    def list(self, request):
        queryset = Booking.objects.all()
        serializer  = BookingSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            reservation = Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return Response({'message': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookingSerializer(reservation, context={'request': request})
        return Response(serializer.data)