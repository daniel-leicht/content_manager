from django.contrib import admin
from .models import Document
from django import forms


class DocumentAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created', 'date_modified')

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(DocumentAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'main_title':
            formfield.widget = forms.TextInput(attrs={'size': '160', 'counted': 'true'})
        return formfield

    class Media:
        js = ('js/jquery.min.js',
              'js/charCount.js',)


# Register models:
admin.site.register(Document, DocumentAdmin)