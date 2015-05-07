from django.contrib import admin
from Audits.models import Audit, Question, Document

# Register your models here.

admin.site.register(Audit)
admin.site.register(Question)
admin.site.register(Document)