from django import forms

from .models import Inquiry

class InquiryForm1(forms.Form):
    # CharFieldはフォームのテキスト型に対応
    name = forms.CharField(
        label='お名前',
        max_length=40, # max_lengthで長さを指定できる
        required=True  # このフォームが入力必須かどうか
    )

    # EmailFieldはフォームのemail型に対応
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
        widget=forms.Textarea # フォームをtextarea要素に変更できる
    )


class InquiryForm2(forms.ModelForm):
    class Meta:
        model = Inquiry # 使用するmodelを指定
        fields = ('name', 'email', 'title', 'contents') # 表示するフォームを指定
