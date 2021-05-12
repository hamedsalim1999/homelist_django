from django.db import models
# Create your models here.
from jalali_date import datetime2jalali, date2jalali
activate=(
("s","سازنده"),
("ma","مصالح فروش"),
("am","املاک"),
("sa","سایر"),
)

from django.db import models
class RoleOne(models.Model):
    create = models.DateTimeField(auto_now_add = True)
    role_name=models.CharField(max_length=512,verbose_name = "مسئول نام" )
    def __str__(self):
        return self.role_name
    class Meta:
        ordering = ('-create',)
        verbose_name = 'سمت '
        verbose_name_plural = 'سمت ها'
class RoleTwo(models.Model):
    create = models.DateTimeField(auto_now_add = True)
    role_name=models.CharField(max_length=512,verbose_name = "مسئول نام" )
    def __str__(self):
        return self.role_name
    class Meta:
        ordering = ('-create',)
        verbose_name = 'سمت '
        verbose_name_plural = 'سمت  ها'
class RoleThree(models.Model):
    create = models.DateTimeField(auto_now_add = True)
    role_name=models.CharField(max_length=512,verbose_name = "مسئول نام" )
    class Meta:
        ordering = ('-create',)
        verbose_name = 'سمت '
        verbose_name_plural = 'سمت ها'
    def __str__(self):
        return self.role_name
class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Form(models.Model):
    id = models.AutoField(primary_key=True)
    create = models.DateTimeField(auto_now_add = True,verbose_name = "تاریخ ایجاد")
    region = models.PositiveBigIntegerField(verbose_name = "منطقه شهرداری")
    district = models.PositiveBigIntegerField(verbose_name = "ناحیه شهرداری ")
    part = models.PositiveBigIntegerField(verbose_name = "بخش شهر داری ")
    type_of_activate  = models.CharField(
        max_length = 2,
        choices = activate,
        verbose_name = "نوع فعالیت",
        )
    responsible_one_name = models.CharField(max_length=1024,verbose_name = " 1 نام مسئول" ,blank=True, null=True)
    responsible_one_phone =  models.CharField(blank=True ,verbose_name="1 شماره تماس مسئول",max_length = 12,blank=True, null=True)
    responsible_one_rule = models.ForeignKey('RoleOne',on_delete=models.CASCADE,blank=True, null=True,verbose_name = "1نقش مسئول")
    responsible_two_name = models.CharField(max_length=1024,verbose_name = "2 نام مسئول",blank=True, null=True)
    responsible_two_phone =  models.CharField(verbose_name="2 شماره تماس مسئول",max_length = 12, blank=True, null=True)
    responsible_two_rule = models.ForeignKey('RoleTwo', on_delete=models.CASCADE,blank=True, null=True,verbose_name = "2نقش مسئول")
    responsible_three_name = models.CharField(max_length=1024,verbose_name = "3 نام مسئول", blank=True, null=True)
    responsible_three_phone =  models.CharField(verbose_name="3 شماره تماس مسئول",max_length = 12, blank=True, null=True)
    responsible_three_rule = models.ForeignKey('RoleThree',on_delete=models.CASCADE,blank=True, null=True ,verbose_name = "3نقش مسئول")
    addres = models.TextField(verbose_name = "نشانی")
    perentage = IntegerRangeField(min_value=0, max_value=100,default=0,verbose_name="درصد پیشرفت")
    start =  IntegerRangeField(min_value=1, max_value=5,default=0,verbose_name="امتیاز")
    def get_created_jalali(self):
        return datetime2jalali(self.create).strftime('%y/%m/%d')
    get_created_jalali.short_description = 'تاریخ شمسی ' 
    get_created_jalali.allow_tags = True
    def __str__(self):
        return self.responsible_one_name
    class Meta:
        ordering = ('-create',)
        verbose_name = 'فرم'
        verbose_name_plural = 'فرم ها'

def get_defualt_objects(obj):
    try:
        obj.objects.last()
    except obj.DoesNotExist:
        None




