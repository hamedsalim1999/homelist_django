from django.contrib import admin
from .models import Form
import csv
from django.http import HttpResponse
from django_jalali.admin.filters import JDateFieldListFilter

#you need import this for adding jalali calander widget

@admin.action(description='خروجی csv')
def export_as_csv(self, request, queryset):

    meta = self.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response
@admin.register(Form)
class FromAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fields  = (
            ('id'),
        
       
        
            ('region', 'district', 'part')
        ,
            ('type_of_activate'),
        
            ('responsible_name','responsible_phone')
        ,
        
            ('manager_name','manager_phone')
        ,
        
            ('addres')
        
        
        
    )
    search_fields = ('responsible_name','manager_name','addres','get_created_jalali')
    list_filter =('create','region','district',)
    list_display = ('create', 'responsible_name','region','district','get_created_jalali')
    actions = [export_as_csv]


