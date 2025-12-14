from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework import status

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(detail=True, methods=['get'])
    def stock(self, request, pk=None):
        item = self.get_object()
        return Response({"stock": item.stock})

    @action(detail=True, methods=['get'])
    def checkout(self, request, pk=None):
        item = self.get_object()
        qty = int(request.data.get("qty", 1))
        item.stock -= qty
        item.save()
        return Response({"remaining_stock": item.stock})