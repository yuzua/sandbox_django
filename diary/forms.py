from django import forms
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください'
    
    def send_email(self):
        subject = 'ほげほげ'
        mail_to = ['hoge@hoge.jp',]
        mail_from = 'piyo@piyo.jp'
        body = 'テストメール'
        mail_msg = EmailMessage(subject=subject, from_email=mail_from, to=mail_to,body=body)
        mail_msg.send()
