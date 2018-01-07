#-*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Content_2, Menu_one, Info_sec, Idea_sec
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect

def main(request):
    items = Menu_one.objects.all()
    briefs = Info_sec.objects.all()
    offers = Idea_sec.objects.all()
    text = Content_2.objects.get()
    context = {'text':text, 'items':items, 'briefs':briefs, 'offers':offers}
    return render(request, 'mainpage/main.html', context)
    
def main_check(request):
    return HttpResponseRedirect(reverse('right_entrance'))

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    send_mail(subject, message, from_email, ['chim73@mail.ru'])
    return HttpResponseRedirect('/#contact')

