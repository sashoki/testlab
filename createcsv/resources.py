from import_export import resources, fields
from .models import Customer

class CustomerResource(resources.ModelResource):

    class Meta:
        model = Customer
        exclude = ('id', )
        fields = ('FirstName', 'LastName', 'BirthDate', 'RegistrationDate', )