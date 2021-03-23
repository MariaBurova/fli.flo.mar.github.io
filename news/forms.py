from .models import Articles
from django.forms import ModelForm,TextInput,DateTimeInput,Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','task','full_text','date','likes']

        widgets = {
            'title':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Заголовок'}),
        'task': TextInput(attrs={
            'class':'form-control',
            'placeholder':'Содержание'
        }),
            'date': DateTimeInput(attrs={
                'class':'form-control',
                'placeholder':'Дата публикации'
            }),
            'full_text':Textarea(attrs={
                'class':'form-control',
                'placeholder':'Текст статьи'
            }),

        }