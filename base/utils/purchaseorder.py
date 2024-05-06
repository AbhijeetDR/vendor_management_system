from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from base.models.purchaseorder import PurchaseOrder
from base.serializers.purchaseorderserializer import PurchaseOrderSerializer

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    # permission_classes = [IsAuthenticated]

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    # permission_classes = [IsAuthenticated]