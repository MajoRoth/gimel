from django.contrib import admin
from Orders.models import Worder, Torder, Aorder
# Register your models here.

admin.site.register(Worder)
admin.site.register(Torder)
admin.site.register(Aorder)

