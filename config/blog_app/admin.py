from django.contrib import admin
from blog_app.models import Publication,Subscriber
class PublicationAdmin(admin.ModelAdmin):
    list_display=('titre','date_publication','nature')
    list_filter=('date_publication','nature')
    search_fields=('titre','contenu')
admin.site.register(Publication,PublicationAdmin)
class SubscriberAdmin(admin.ModelAdmin):
    list_display=('email','date_abonnement')
    list_filter=('date_abonnement',)
    search_fields=('email',)
admin.site.register(Subscriber,SubscriberAdmin)