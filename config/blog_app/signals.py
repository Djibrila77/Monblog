from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mass_mail

from .models import Publication, Subscriber 

@receiver(post_save, sender=Publication)
def send_newsletter_on_post(sender, instance, created, **kwargs):
    if created:  # On vérifie que c'est une création, pas une simple modification
        subscribers = Subscriber.objects.all()
        if subscribers.exists():
            subject = f"Nouvel article : {instance.titre}"
            message = f"Bonjour ! Un nouvel article vient d'être publié : {instance.titre}.\n\nDécouvrez-le ici : https://monblog.f2p8.onrender.com/post/{instance.slug}"
            from_email = 'djibrila6299@gmail.com'
            
            # On prépare la liste des mails (un mail pour chaque abonné)
            mails = [
                (subject, message, from_email, [sub.email]) 
                for sub in subscribers
            ]    
            # Envoi groupé (plus rapide et efficace)
            send_mass_mail(mails, fail_silently=False)