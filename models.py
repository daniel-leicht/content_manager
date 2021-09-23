from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.html import format_html


class RichContent(models.Model):
    title = models.CharField(
        blank=False, null=False, max_length=150,
        help_text="Enter an internal title for this content, this is for internal use and not displayed to users."
    )
    content = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_html(self):
        if self.content:
            return format_html(self.content)
        else:
            return ""

    def __str__(self):
        return "%s Content" % self.title


class Document(models.Model):
    main_title = models.CharField(max_length=250, help_text="Main document header, this should be the H1 tag unless "
                                                            "mentioned otherwise.")
    content = models.ForeignKey(RichContent, help_text="The main content of this document", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Document: %s" % self.main_title
