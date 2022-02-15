from django.shortcuts import render

# Create your views here.
# from .serializers import User_info_Serializers
# from rest_framework import viewsets
# from .models import User_info
from rest_framework import viewsets
from .serializers import User_info_Serializers
from .models import User_info



def index(request):
    return render(request, "index.html")


class UserView(viewsets.ModelViewSet):
    serializer_class =User_info_Serializers
    queryset = User_info.objects.all()