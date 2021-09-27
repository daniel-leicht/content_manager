from django.contrib import admin
from .models import Document


class DocumentAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_modified')


# Register models:
admin.site.register(Document, DocumentAdmin)