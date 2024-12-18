from django import forms
from .models import Pipeline, Product, Batch, Separator, QualityControl, Report

from django import forms
from .models import Pipeline

class PipelineForm(forms.ModelForm):
    class Meta:
        model = Pipeline
        fields = ['length', 'diameter', 'material', 'status']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'pipeline', 'volume', 'order']

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['user', 'type', 'volume', 'quality']

class SeparatorForm(forms.ModelForm):
    class Meta:
        model = Separator
        fields = ['pipeline', 'status', 'fill_level']

class QualityControlForm(forms.ModelForm):
    class Meta:
        model = QualityControl
        fields = ['batch', 'data']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['user', 'pipeline', 'volume', 'quality']

from django import forms
from .models import System, Route

class SystemForm(forms.ModelForm):
    class Meta:
        model = System
        fields = ['name', 'startDate', 'endDate', 'status']

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['startPoint', 'endPoint', 'volume', 'productType']


