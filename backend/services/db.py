from mongoengine import connect
from datetime import datetime

from config.settings import db_settings
from models.user import User
from models.image import Image

def connect_mongo_db():
    """Connect to the Database
    """
    connect(db=db_settings.db_name, host=db_settings.db_host, port=db_settings.db_port)

def insert_one_user(Object : User):
    """Insert One Record in Database

    Args:
        Object (User): Object of the User
    """
    Object.save()

def search_by_email(email : str) -> User:
    """Search Record By Email

    Args:
        email (str): Email ID of the User

    Returns:
        User: Object of the data
    """
    user_data = User.objects(email = email)
    return user_data

def check_user_data(email: str, password: str) -> int:
    """Check User is valid or Not

    Args:
        email (str): User Emial ID
        password (str): User Password

    Returns:
        Code: 100 = User is Valid.
              102 = User is not Valid. 
    """
    user_data = User.objects(email = email)
    for i in user_data:
        if i.email == email and i.password == password:
            return 100
    else:
        return 102

def insert_one_user_image(Object: Image) -> None:
    Object.save()

def insert_or_update_user_image(file_name: str, email: str, url: str) -> None:
    images_list = Image.objects(email = email, filename = file_name)
    if images_list:
        images_list.update(updated_at = datetime.utcnow())
    else:
        image_object = Image(email = email, filename = file_name, url = url)
        image_object.validate()
        image_object.save()

def get_user_images_by_email(email: str) -> list:
    user_data = Image.objects(email = email)
    user_images = []
    for i in user_data:
        user_images.append(i.url)
    return user_images

def update_user_detailsby_email(body: dict) -> None:
    User.objects(email = body["email"]).update_one(set__first_name = body["first_name"], set__last_name = body["last_name"], set__password = body["password"])