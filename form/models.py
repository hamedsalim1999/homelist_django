from django.db import models
from phone_field import PhoneField
# Create your models here.
from jalali_date import datetime2jalali, date2jalali

class Form(models.Model):
    id = models.AutoField(primary_key=True)
    create = models.DateTimeField(auto_now_add = True,verbose_name = "تاریخ ایجاد")
    region = models.PositiveBigIntegerField(verbose_name = "منطقه شهرداری")
    district = models.PositiveBigIntegerField(verbose_name = "ناحیه شهرداری ")
    part = models.PositiveBigIntegerField(verbose_name = "بخش شهر داری ")
    type_of_activate  = models.TextField(verbose_name = "نوع فعالیت")
    responsible_name = models.CharField(max_length=1024,verbose_name = "نام مسئول")
    responsible_phone = PhoneField(blank=True, help_text='Contact phone number',verbose_name = "شماره تماس مسئول")
    manager_name = models.CharField(max_length=1024, verbose_name = "نام مدیر")
    manager_phone = PhoneField(blank=True, help_text='Contact phone number',verbose_name = "شماره تماس مدیر")
    addres = models.TextField(verbose_name = "نشانی")

    def get_created_jalali(self):
        return datetime2jalali(self.create).strftime('%y/%m/%d _ %H:%M:%S')
    get_created_jalali.short_description = 'تاریخ شمسی ' 
    get_created_jalali.allow_tags = True
    def __str__(self):
        return self.responsible_name
    class Meta:
        ordering = ('-create',)
        verbose_name = 'فرم'
        verbose_name_plural = 'فرم ها'

