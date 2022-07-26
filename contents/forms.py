from django.forms import ModelForm, TextInput, Textarea, HiddenInput
from .models import Thread, Comment
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class ThreadForm(ModelForm):

    class Meta:
        model = Thread
        fields = ['article', 'name', 'email', 'message']
        widgets = {
            'article': HiddenInput(),
            'name': TextInput(attrs={'placeholder': '氏名/ニックネームを入力してください。'}),
            'email': TextInput(attrs={'placeholder': 'メールアドレスを入力してください。'}),
            'message': Textarea(attrs={'cols': 1, 'rows': 15})
        }

        # def validate(self, value):
        #     super().validate(value)
        #     validate_email(value['email'])


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['thread', 'name', 'email', 'message']
        widgets = {
            'thread': HiddenInput(),
            'name': TextInput(attrs={'placeholder': '氏名/ニックネームを入力してください。'}),
            'email': TextInput(attrs={'placeholder': 'メールアドレスを入力してください。'}),
            'message': Textarea(attrs={'cols': 1, 'rows': 15})
        }