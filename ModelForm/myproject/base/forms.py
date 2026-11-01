from django import forms 
from .models import CarModel

class Carforms(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = "__all__"  #[car,color,price]
        
        labels = {
            'car' : 'car_name',
            'color' : 'shades',
            'price' : 'paise'
        }
        
        widgets = {
            'car':forms.TextInput(
                attrs = {
                    'placeholder':'enter the car name',
                    'class' : 'car_class'
                }
            ),
            
            'color':forms.TextInput(
                attrs = {
                    'placeholder':'enter the color name',
                    'class' : 'car_class'
                }
            ),
            
            
            'price':forms.TextInput(
                attrs = {
                    'placeholder':'enter the price name',
                    'class' : 'car_class'
                }
            ),
        }