<<<<<<< HEAD
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import InquiryForm

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class InquiryView(FormView):
=======
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

from .forms import InquiryForm

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
>>>>>>> master
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

<<<<<<< HEAD
    def form_vaild(self,form):
        form.send_email()
        return super().form_vaild(form)
=======
    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        return super().form_valid(form)
>>>>>>> master
