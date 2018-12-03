# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from datetime import datetime


class Order(models.Model):
    class Meta():
        ordering = ['-ProductName', '-OrderCreateDate']
        db_table = 'orders'

    ProductName = models.CharField(max_length=100, verbose_name='Product name')
    OrderCreateDate = models.DateField(default=timezone.now)

    def __str__(self):
        return self.ProductName

class Customer(models.Model):
    class Meta():
        ordering = ['-RegistrationDate', 'LastName']
        db_table = 'customer'
        verbose_name_plural = 'Customer'
        verbose_name = 'Customers'

    FirstName = models.CharField(max_length=30, verbose_name=u'Customer name')
    LastName = models.CharField(max_length=30, verbose_name=u'Customer surname')
    BirthDate = models.DateField(verbose_name=u'Customer birthday')
    RegistrationDate = models.DateField(verbose_name=u'Date registration')
    CustomOder = models.ForeignKey(Order, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.FirstName, self.LastName)




