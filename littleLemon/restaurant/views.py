from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import booking, menu
from .serializers import bookingSerializer, menuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = menuSerializer
    queryset = menu.objects.all()

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = bookingSerializer
    queryset = booking.objects.all()


# class menuview(APIView):
#     def post(self, request):
#         serializer = menuSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})