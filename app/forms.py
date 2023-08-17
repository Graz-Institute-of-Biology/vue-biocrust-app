from django import forms

from .models import Document, DLModel, DSetDocument

class UploadForm(forms.ModelForm):
    class Meta:
        model = DSetDocument
        fields = ('document', 'name')

class ModelUploadForm(forms.ModelForm):
    class Meta:
        model = DLModel
        fields = ('document',)