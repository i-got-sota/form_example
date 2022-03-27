from django.db import models


class Inquiry(models.Model):
    name = models.CharField('お名前', max_length=40)
    email = models.EmailField('メールアドレス')
    title = models.CharField('件名', max_length=128)
    contents = models.TextField('内容')
    posted_at = models.DateTimeField('お問い合わせ日時', auto_now_add=True)

    def __str__(self):
        return self.title
