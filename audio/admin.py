from django.contrib import admin
from .models import Audio, Host, Contact, Social, Donate_Option, Partner

# Register your models here.
admin.site.register(Audio)
admin.site.register(Host)
admin.site.register(Contact)
admin.site.register(Social)
admin.site.register(Donate_Option)
admin.site.register(Partner)