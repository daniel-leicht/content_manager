from django.contrib import admin
from .models import RichContent, Document


class RichContentAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_modified')


class DocumentAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_modified')


# Register models:
admin.site.register(RichContent, RichContentAdmin)
admin.site.register(Document, DocumentAdmin)