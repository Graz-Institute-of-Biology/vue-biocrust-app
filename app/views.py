from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Posts, Tests, Image, ImageNew, Document
from .serializers import PostSerializer, TestSerializer, ImageSerializer, ImageNewSerializer, PredSerializer
from django.shortcuts import render
from django.http import JsonResponse
from .models import PredResults
import numpy as np
import sys
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import UploadForm, ModelUploadForm
# Create your views here.

    
class TestsView(generics.RetrieveAPIView):
    queryset = Tests.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data)
    
class ImageView(generics.RetrieveAPIView):
    queryset = Image.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ImageSerializer(queryset, many=True)
        return Response(serializer.data)
    
class ImageNewView(generics.RetrieveAPIView):
    queryset = Document.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ImageNewSerializer(queryset, many=True)
        return Response(serializer.data)

class PostsView(generics.ListCreateAPIView):

    serializer_class = PredSerializer

    def get(self, request, *args, **kwargs):

        sepal_length = float(self.request.GET.get('sepal_length'))
        sepal_width = float(self.request.GET.get('sepal_width'))
        petal_length = float(self.request.GET.get('petal_length'))
        petal_width = float(self.request.GET.get('petal_width'))

        result = str(np.sum([sepal_length, sepal_width, petal_length, petal_width]))
        serializer = PredSerializer(data=self.request.GET)
        if serializer.is_valid():
            serializer.save()
            return Response(result)
        return Response(serializer.errors, status=400)


@csrf_exempt 
def index(request):
    form = UploadForm()
    files = Document.objects.all()
    context = {'files': files}
    return render(request, 'src/Pages/Upload.vue', {'form': form}, context)

@csrf_exempt 
def upload(request):
    if request.FILES:
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
    
    return JsonResponse({'success': True})

@csrf_exempt 
def uploadmodel(request):
    if request.FILES:
        form = ModelUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
    
    return JsonResponse({'success': True})