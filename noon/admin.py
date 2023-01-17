from django.contrib import admin
from noon.models import Web

# Register your models here.
class WebAdmin(admin.ModelAdmin):
    all_data = ('Name', 'Data')


admin.site.register(Web,WebAdmin)
