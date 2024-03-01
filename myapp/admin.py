from django.contrib import admin
from myapp.models import DeviceCoverage,Categories,Device

# Register your models here.

admin.site.register(DeviceCoverage)
admin.site.register(Categories)
admin.site.register(Device)

