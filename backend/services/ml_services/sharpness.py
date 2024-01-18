# import cv2
# TODO: Change to Opencv
from PIL import Image, ImageEnhance
import numpy as np
import cv2

from services.file import save_to_final_folder, save_to_sub_folder, create_copy_image, check_copy_file_exist, delete_copy_file, revert_operation
from config.settings import file_structure

def sharpness_fun(file_name: str, system_file_path: str, factor: int, save: int, revert: int) -> str:
    sharpness_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.SHARPNESS_PATH + system_file_path.split("/")[-1]
    operation_file_path = check_copy_file_exist(original_path = system_file_path, sub_path = sharpness_path, file_name = file_name)
    image = Image.open(operation_file_path)
    enhancer = ImageEnhance.Sharpness(image)
    sharpness_image = enhancer.enhance(factor)
    sharpness_image = np.array(sharpness_image)
    sharpness_image = cv2.cvtColor(sharpness_image, cv2.COLOR_BGR2RGB)
    if operation_file_path == system_file_path:
        create_copy_image(from_path = system_file_path, to_path = sharpness_path, file_name = file_name)
    save_to_sub_folder(sharpness_path, sharpness_image)
    save_to_final_folder(system_file_path, sharpness_image)
    if save == 1:
        delete_copy_file(sub_path = sharpness_path, file_name = file_name)
    if revert == 1:
        revert_operation(original_path = system_file_path, sub_path = sharpness_path, file_name = file_name)
    return system_file_path