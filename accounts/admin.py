from django.contrib.admin import *
from .models import *

class DisplaySettingAdmin(ModelAdmin):
    list_display = ['user', 'dark_mode', 'small_text']

site.register(DisplaySetting, DisplaySettingAdmin)



class ResidenceAdmin(ModelAdmin):
		list_display = ["user", "street", "province", "code"]

site.register(Residence, ResidenceAdmin)



class ContactDetailAdmin(ModelAdmin):
	list_display = ["user", "call", "email"]

site.register(ContactDetail, ContactDetailAdmin)
