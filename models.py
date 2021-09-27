from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html


class Document(models.Model):
    main_title = models.CharField(max_length=250, help_text="Main document header, this should be the H1 tag unless "
                                                            "mentioned otherwise.")
    content = RichTextField(help_text="Keep empty to display default (if default exists)")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_html(self):
        if self.content:
            return format_html(self.content)
        else:
            return ""

    def __str__(self):
        return "Document: %s" % self.main_title
