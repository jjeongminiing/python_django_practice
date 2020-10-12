from django.contrib import admin
from .models import Muser

# Register your models here.


class MuserAdmin(admin.ModelAdmin):
    list_display = ('email', )


admin.site.register(Muser, MuserAdmin)
