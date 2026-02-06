from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Publication, Subscriber
from .forms import ContactForm, NewsletterForm

def home_view(request):
    articles = Publication.objects.filter(nature=Publication.Nature.ARTICLE)
    competences = Publication.objects.filter(nature=Publication.Nature.COMPETENCE)
    contact_form = ContactForm()
    newsletter_form = NewsletterForm()
    
    if request.method == 'POST':
        if 'contact_submit' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                nom = contact_form.cleaned_data['nom']
                email = contact_form.cleaned_data['email']
                message = contact_form.cleaned_data['message']
                
                send_mail(
                    f'Message de {nom}',
                    f'Email: {email}\n\n{message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                
                return redirect('blog_app:confirmation')
        
        elif 'newsletter_submit' in request.POST:
            newsletter_form = NewsletterForm(request.POST)
            if newsletter_form.is_valid():
                email = newsletter_form.cleaned_data['email']
                Subscriber.objects.get_or_create(email=email)
                
                return redirect('blog_app:confirmation')
    
    return render(request, 'page.html', {
        'articles': articles,
        'competences': competences,
        'contact_form': contact_form,
        'newsletter_form': newsletter_form,
    })

def confirmation_view(request):
    return render(request, 'confirmation.html')