# -*- coding: utf-8 -*-

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from createcsv.models import Customer, Order
from createcsv.resources import CustomerResource

# Register your models here.

class CustomerResource(resources.ModelResource):

    class Meta:
        model = Customer
        import_id_fields = ('FirstName', )
        fields = ('FirstName', 'LastName', 'BirthDate', 'RegistrationDate', )

class OrderAdmin(admin.ModelAdmin):
    fields = ['ProductName', 'OrderCreateDate']
    list_display = ('ProductName', 'OrderCreateDate')


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource
    list_display = ('id', 'FirstName', 'LastName', 'BirthDate', 'RegistrationDate', 'CustomOder')
    search_fields = ['LastName', 'BirthDate', 'RegistrationDate']



admin.site.register(Order, OrderAdmin)
# admin.site.register(Customer, CustomerAdmin)

