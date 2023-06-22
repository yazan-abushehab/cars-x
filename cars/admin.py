from django.contrib import admin
from .models import Car

# Register your models here.

class CustomCarAdmin(admin.ModelAdmin):
    model = Car
    list_display = ['name', 'purchaser', 'description',]
    fieldsets = (
        ('Owner',{
            'fields':('purchaser',
             )}
        ),
        ('car info',{
            'fields':('name','description',
             )}
        )
    )

admin.site.register(Car, CustomCarAdmin)