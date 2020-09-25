from django import forms
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):
    name = forms.CharField(label="お名前",max_length=100)
    mail = forms.CharField(label="メールアドレス",max_length=100)
    title = forms.CharField(label="タイトル",max_length=100)
    message = forms.CharField(label="メッセージ",widget=forms.Textarea)

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['name'].widget.attrs['class'] = 'form-control.col-9'
    #     self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください'

    def send_email(self):
        subject = 'sample'
        mail_to = ['sample@mail.com']
        mail_from = 'sample@sample.jp'
        body = 'テストメール'
        mail_msg = EmailMessage(subject=subject,from_mail=mail_from,to=mail_to,body=body)
        mail_msg.send()
