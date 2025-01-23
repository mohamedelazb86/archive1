from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Document_Type,Sector


class SectorAdmin(SummernoteModelAdmin):
    list_display=['code','name']
    search_fields=['name','notes']

    summernote_fields = ('notes',)


admin.site.register(Document_Type)
admin.site.register(Sector,SectorAdmin)