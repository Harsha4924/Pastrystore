from django import forms
from .models import ItemsDelivery

class ItemsDeliveryForm(forms.ModelForm):
    
    class Meta:
        model = ItemsDelivery
        fields = '__all__'
        exclude = ['order_id','contact_number',]
        labels = {
            "Name": "Your Name",
            "contact_number": "Mobile Number",
            "address": "Address",
            "zip_code": "Zip code",
            "City": "City",
            "State": "State",
        }
        # error_messages = {
        #     "Name": {
        #         "required": "Your Name must not be empty",
        #         "max_length": "Please enter a shorter name"
        #     }
        # }
















# CREATE TABLE Profile_Configuration (
#     id SERIAL PRIMARY KEY,
#     Acceptable_formats VARCHAR(200),
#     Acceptable_Types VARCHAR(200),
#     Template VARCHAR(200),
#     Status VARCHAR(50)
# );

# INSERT INTO Profile_Configuration (Acceptable_formats, Acceptable_Types, Template, Status)

# VALUES('XML','R3',"",'Active'),
#       ('XML','R2','','Active'),
#       ('PDF','CIOMS','','Active'),
#       ('PDF','Medwatch','','Active'),
#       ('PDF','ADE','','Inactive'),
#       ('PDF','Custom forms','','Inactive');