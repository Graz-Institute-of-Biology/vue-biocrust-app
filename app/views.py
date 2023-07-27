from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Posts, Tests, Image, ImageNew, Document, DLModel, ImageDoc, DSetDocument, Dataset
from .serializers import PostSerializer, TestSerializer, ImageSerializer, ImageNewSerializer, PredSerializer, DatasetSerializer, ModelSerializer
from django.shortcuts import render
from django.http import JsonResponse
from .models import PredResults
import numpy as np
import sys
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.http import JsonResponse
from .forms import UploadForm, ModelUploadForm
from rest_framework.views import APIView
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
    queryset = DSetDocument.objects.all()#values_list('name', flat=True)
    names = DSetDocument.objects.values_list('name', flat=True)
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ImageNewSerializer(queryset, many=True)
        return Response(serializer.data)
    
class GetModelsView(generics.RetrieveAPIView):
    queryset = DLModel.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ModelSerializer(queryset, many=True)
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
    
class DatasetListCreateView(generics.RetrieveAPIView):
    queryset = Dataset.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = DatasetSerializer(queryset, many=True)
        return Response(serializer.data)


@csrf_exempt 
def index(request):
    form = UploadForm()
    files = Document.objects.all()
    context = {'files': files}
    return render(request, 'src/pages/Upload.vue', {'form': form}, context)

@csrf_exempt 
def getimg(request):
    imgs = Document.objects.all() #filter(file_type='document')
    context = {'images': imgs}
    return render(request, 'src/pages/ImageNew.vue', context)
    #return Response(imgs)

@csrf_exempt 
def get_images(request):
    if request:
        images = DSetDocument.objects.all() #.values_list('image', flat=True)
        
        paths = []
        for image_path in images:
            #image_url = default_storage.url(image_path)
            paths.append(image_path)
            print(image_path)
        return JsonResponse({'image_paths': paths})
    print('dere')

@csrf_exempt 
def upload(request):
    if request:
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
    
            return JsonResponse({'success': True})
        
        else:
            return JsonResponse({'success': False})

@csrf_exempt 
def uploadmodel(request):
    if request.FILES:
        form = ModelUploadForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
    
    return JsonResponse({'success': True})

@csrf_exempt 
def datasetupload(request):
    serializer = DatasetSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'success': True})
    
class DatasetUploadView(APIView):
    def post(self, request, format=None):
        content_type = request.content_type
        if content_type.startswith('multipart/form-data'):
            # Handle file upload using request.FILES
            dataset_name = request.POST.get('dataset_name')
            description = request.POST.get('description')
            coordinates = request.POST.get('coordinates')
            #names = Dataset.objects.all().filter('dataset_name')
            if Dataset.objects.filter(dataset_name=dataset_name).exists():
                return Response({"message": "Name already in use"}, status=400)
            
            # Save the Dataset to the database
            dataset = Dataset(dataset_name=dataset_name, description=description, coordinates=coordinates)
            dataset.save()
            
            return Response({"message": "Upload successful"}, status=201)