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
        self.fields['name'].widget = forms.Textarea(attrs={
            'class': 'display-6 logo-font text-black form-h1-size w-100',
            'rows': 1,  # Set initial row count to 1 for header-like appearance
            'placeholder': 'Enter workout name'
        })
        self.fields['fitness'].label = ''
        self.fields['sport'].label = ''
        self.fields['level'].label = ''
        self.fields['name'].label = ''
        self.fields['description'].label = ''
        self.fields['price'].label = ''
        
        self.fields['description'].widget = forms.Textarea(attrs={
            'class': 'lead text-muted text-black form-p-size w-100',
            'rows': 3,  # Adjust rows as needed for the initial height
            'placeholder': 'Enter description here'
})


        
