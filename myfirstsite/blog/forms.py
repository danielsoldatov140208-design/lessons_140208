from django import forms 
from .models import Book, Student

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'price']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'group'] 


    name = forms.CharField(label='Name', max_length=100, required=True)
    age = forms.IntegerField(label='Age',required=True)
    email = forms.EmailField(label='Email',required=True)
    group = forms.CharField(label='Groop', max_length=10, required=True )
    
    def clean (self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        age = cleaned_data.get('age')
        email = cleaned_data.get('email')
        group = cleaned_data.get('groop')

        if len(name)<3:  
            raise forms.ValidationError("Имя слишком короткое")
        
        if any(ch.isdigit() for ch in name):
            raise forms.ValidationError("Имя не должно содержать цифры")
        
        if age>40:
            raise forms.ValidationError("Возраст должен быть не более 40 лет")

        
        if age<16:
            raise forms.ValidationError("Возраст должен быть не менее 16 лет")
        if group:
            if not group.startswith("IT-"):
                raise forms.ValidationError("Группа должна начинаться с 'IT-'")
