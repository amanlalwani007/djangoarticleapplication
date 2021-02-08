from django.contrib import admin
from .models import Tutorial,TutorialSeries,TutorialCategory
# Register your models here.
from tinymce.widgets import TinyMCE
from django.db import models

class TutorialAdmin(admin.ModelAdmin):
    ##  benefit if you want to edit only some fields and rest are default so in that case you  can define 
    # what colums you want to show in admin panel 
    # fields =["tutorial_title",
    # "tutorial_publish",
    # "tutorial_content"]
    ### clustering in admin panel 
    fieldsets = [
        ("Title/date",{"fields":["tutorial_title","tutorial_published"]}),

        ("URL",{"fields":["tutorial_slug"]}),
        ("Series",{"fields":["tutorial_series"]}),
        ("Content",{"fields":["tutorial_content"]})
    ]
    formfield_overrides={
        models.TextField:{'widget': TinyMCE()}
    }


admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorial,TutorialAdmin)
