from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import *

from django.contrib import admin
admin.autodiscover()

router = DefaultRouter()
router.register(r'orders', OrderList),
router.register(r'customers', CustomerList)

urlpatterns = router.urls

# urlpatterns = [
#
#     #url(r'^$', 'createcsv.views.portfolios', name='portfolios'),
#
#     ]
