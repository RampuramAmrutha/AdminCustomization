from django.contrib import admin

# Register your models here.


from app.models import *
class CustomizedWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_display_links=['topic_name','name']
    list_editable=['url']
    search_fields=['name']
    list_per_page=1
    list_filter=['name','url']
class CustomizedAccessRecord(admin.ModelAdmin):
    list_display=['name','author','date']
    list_display_links=['name']
    list_editable=['date']
    search_fields=['author']
    list_filter=['date']



admin.site.register(Topic)
admin.site.register(Webpage,CustomizedWebpage)
admin.site.register(AccessRecord,CustomizedAccessRecord)