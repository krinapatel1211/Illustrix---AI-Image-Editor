import os
from config.settings import file_structure
import cv2
import numpy as np
import base64
import random
import string
import shutil

def create_base_structure(email: str) -> None:
    base_folder = file_structure.USER_DATA + email
    
    is_exist = os.path.exists(base_folder)
    if is_exist == False:
        os.mkdir(base_folder)
        for i in file_structure.BASE_STRUCTURE:
            sub_folders_path = base_folder + i
            os.mkdir(sub_folders_path)

def get_file_path_from_url(body: dict) -> str:
    global_url = body["image_url"]
    file_name = body["image_url"].split("/")[-1]
    system_path_index = body["image_url"].find("/static")
    system_path = "." + body["image_url"][system_path_index:]
    background_image = ""
    factor = 0
    save = 1
    revert = 0
    if "background_url" in body:
        background_image_index = body["background_url"].find("/static")
        background_image = "." + body["background_url"][background_image_index:]
    if "factor" in body:
        factor = body["factor"]
    if "save" in body:
        save = body["save"]
    if "revert" in body:
        revert = body["revert"]
    return file_name, system_path, global_url, background_image, factor, save, revert

def save_to_final_folder(path: str, image: np.ndarray) -> None:
    cv2.imwrite(path, image)

def save_to_sub_folder(path: str, image: np.ndarray) -> None:
    cv2.imwrite(path, image)

def generate_random_string() -> str:
    random_string = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    return random_string

def upload_image(email: str, base_64_string: str) -> str:
    image = base64.b64decode(base_64_string, validate=True)
    upload_path = file_structure.USER_DATA + email + file_structure.UPLOAD_PATH
    file_name = generate_random_string() + ".png"
    file_path = upload_path + file_name
    final_file_path = file_structure.USER_DATA + email + file_structure.FINAL_IMAGE_PATH + "/" + file_name
    with open(final_file_path, "wb") as f:
        f.write(image)
    with open(file_path, "wb") as f:
        f.write(image)
    global_path = file_structure.SERVER_URL + final_file_path[2:]
    return global_path, file_name

def create_copy_image(from_path: str, to_path: str, file_name: str) -> str:
    last_slash_index = to_path.rfind("/")
    copy_path = to_path[:last_slash_index + 1] + file_name.split(".")[0] + file_structure.COPY_FILE_SUFFIX + "." + file_name.split(".")[-1]
    shutil.copy(from_path, copy_path)

def check_copy_file_exist(original_path: str,sub_path: str, file_name: str) -> bool:
    file = file_name.split(".")[0]
    copy_path = sub_path.replace(file, file + file_structure.COPY_FILE_SUFFIX)
    if os.path.exists(copy_path):
        print("check_copy", copy_path)
        return copy_path
    else:
        print("check_copy", original_path)
        return original_path

def delete_copy_file(sub_path: str, file_name: str) -> None:
    print("delete")
    print(sub_path)
    file = file_name.split(".")[0]
    delete_path = sub_path.replace(file, file + file_structure.COPY_FILE_SUFFIX)
    print(delete_path)
    print("delete")
    os.remove(delete_path)

def revert_operation(original_path: str, sub_path: str, file_name: str) -> None:
    print("revert")
    print(sub_path)
    file = file_name.split(".")[0]
    copy_path = sub_path.replace(file, file + file_structure.COPY_FILE_SUFFIX)
    print(copy_path)
    print("revert")
    shutil.copy(copy_path, original_path)
    shutil.copy(copy_path, sub_path)
    os.remove(copy_path)