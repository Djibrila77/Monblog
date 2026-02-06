from django import forms
class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, label="Votre nom")
    email = forms.EmailField(label="Votre email")
    message = forms.CharField(widget=forms.Textarea, label="Message")

class NewsletterForm(forms.Form):
    email = forms.EmailField(label="EMAIL")
    case=forms.BooleanField(label="Oui.Abonnez-moi a votre newsletter")