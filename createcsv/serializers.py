from rest_framework import serializers

from createcsv.models import Order, Customer

class OrderSerializer(serializers.ModelSerializer):
        class Meta:
                model = Order
                fields = (
                        'id',
                        'ProductName',
                        'OrderCreateDate',
                )


class CustomerSerializer(serializers.ModelSerializer):
        class Meta:
                model = Customer
                fields = (
                        'id',
                        'FirstName',
                        'LastName',
                        'BirthDate',
                        'RegistrationDate',
                        'CustomOder',
                )
