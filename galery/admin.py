from django.contrib import admin
from galery.models import GalerieSeite, Bild

class BildInline(admin.TabularInline):
    model = Bild
    extra = 10


class GSeiteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['titel','seite_url','isdeleted','dateiname_img']}),
        ('Text', {'fields': ['text'], 'classes': ['collapse']}),
    ]
    inlines = [BildInline]

admin.site.register(GalerieSeite, GSeiteAdmin)
