from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import ItemSerializer
from .models import Item

# Create your views here.

def index (request):
    return render(request,'items/index.html')
    
def index2(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ItemViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer

    """
    queryset = Item.objects.all().order_by('id')
    """

    def get_queryset(self):
    	queryset = Item.objects.all().order_by('id')
    	uniqueValue = self.request.query_params.get('sys_id')
    	if uniqueValue is not None:
    		queryset = queryset.filter(uniqueValue=uniqueValue)
    	return queryset