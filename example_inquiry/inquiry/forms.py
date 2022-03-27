from django import forms

from .models import Inquiry

class InquiryForm1(forms.Form):
    name = forms.CharField(
        label='お名前',
        max_length=40,
        required=True
    )

    email = forms.EmailField(
        label='メールアドレス',
        required=True
    )

    title = forms.CharField(
        label='タイトル',
        required=True
    )

    contents = forms.CharField(
        label='内容',
        widget=forms.Textarea
    )

