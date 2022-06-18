from django.contrib import admin
from .models import NeighbourHood,Business,Post,EmergencyService
# Register your models here.
admin.site.register(NeighbourHood)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(EmergencyService)
