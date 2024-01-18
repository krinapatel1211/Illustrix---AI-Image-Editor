from mongoengine import Document, StringField, DateTimeField, EmailField
from datetime import datetime

class Image(Document):
    email = EmailField(required=True)
    filename = StringField(required=True)
    url = StringField(required=True)
    created_at = DateTimeField(default = datetime.utcnow())
    updated_at = DateTimeField(default =  datetime.utcnow())