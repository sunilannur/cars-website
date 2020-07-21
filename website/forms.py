from django import forms
from .models import *


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('name','detail','price','model','phone','mileage')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'detail': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'model': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'mileage': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'body_style': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'transmission': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'exterior_color': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'drivetrain': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'cylinder_count': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'seller_type': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'fuel': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            # 'car_image': forms.FileInput(attrs={'class': 'form-control'}),

        }


class MakerForm(forms.ModelForm):
    class Meta:
        model = Maker
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }


class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = '__all__'

        widgets = {
            'maker': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }


class TransmissionForm(forms.ModelForm):
    class Meta:
        model = Transmission
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }


class CylinderForm(forms.ModelForm):
    class Meta:
        model = Cylinder
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }


class DrivetrainForm(forms.ModelForm):
    class Meta:
        model = Drivetrain
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }


class SellerTypeForm(forms.ModelForm):
    class Meta:
        model = SellerType
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }


class FuelForm(forms.ModelForm):
    class Meta:
        model = Fuel
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }


class BodyForm(forms.ModelForm):
    class Meta:
        model = Body
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
        }
