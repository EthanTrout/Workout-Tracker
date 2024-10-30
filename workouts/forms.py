from django import forms
from .models import Workout, Fitness, Sport, Level

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = [
            'fitness', 
            'sport', 
            'level', 
            'name', 
            'description', 
            'price', 
            'rating', 
            'image_url', 
            'image'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'price': forms.NumberInput(attrs={'step': 0.01}),
            'rating': forms.NumberInput(attrs={'step': 0.1}),
        }
    
    # Override the __init__ method to populate the choice fields
    def __init__(self, *args, **kwargs):
        super(WorkoutForm, self).__init__(*args, **kwargs)
        self.fields['fitness'].queryset = Fitness.objects.all()
        self.fields['sport'].queryset = Sport.objects.all()
        self.fields['level'].queryset = Level.objects.all()
