from django.forms import ModelForm, TextInput, Textarea
from .models import Comment


class ContactForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'title', 'message']
        widgets = {
            'name': TextInput(attrs={'placeholder': '氏名/ニックネームを入力してください。'}),
            'email': TextInput(attrs={'placeholder': 'メールアドレスを入力してください。'}),
            'title': TextInput(attrs={'placeholder': '件名を入力してください。'}),
            'message': Textarea(attrs={'cols': 1, 'rows': 15})
        }
