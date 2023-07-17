from django import forms

from .models import Document, DLModel

class UploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)

class ModelUploadForm(forms.ModelForm):
    class Meta:
        model = DLModel
        fields = ('document',)