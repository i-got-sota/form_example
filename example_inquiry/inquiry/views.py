from django.shortcuts import render, redirect

from .models import Inquiry
from .forms import InquiryForm1, InquiryForm2

def inquiry1(request):
    """forms.Formを用いたお問い合わせ"""
    if request.method == 'POST':
        # フォーム送信データを受け取る
        form = InquiryForm1(request.POST)
        if form.is_valid():
            inquiry = Inquiry()

            # バリデーションを通過したデータをセット
            inquiry.name = form.cleaned_data['name']
            inquiry.email = form.cleaned_data['email']
            inquiry.title = form.cleaned_data['title']
            inquiry.contents = form.cleaned_data['contents']
            
            Inquiry.objects.create(
                name=inquiry.name,
                email=inquiry.email,
                title=inquiry.title,
                contents=inquiry.contents
            )
            return redirect('inquiry_done')

    else:
        form = InquiryForm1()

    return render(request, 'inquiry/inquiry.html', {'form': form})

def inquiry2(request):
    """forms.ModelFormを用いたお問い合わせ"""
    if request.method == 'POST':
        # フォーム送信データを受け取る
        form = InquiryForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inquiry_done')

    else:
        form = InquiryForm2()

    return render(request, 'inquiry/inquiry.html', {'form': form})

def done(request):
    """お問い合わせ完了ページ"""
    return render(request, 'inquiry/done.html')            
