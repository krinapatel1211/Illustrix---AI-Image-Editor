import cv2

from services.ml_services.background_remove import background_remove_fun
from services.ml_services.background_blur import background_blur_fun
from services.ml_services.merge_two_images import merge_two_images_fun
from services.file import save_to_final_folder

def self_background_blur_fun(file_name: str, system_file_path: str) -> str:
    blurred_bg = background_blur_fun(file_name = file_name, system_file_path = system_file_path)
    bg_remove = background_remove_fun(file_name = file_name, system_file_path = system_file_path)
    combined_image_path = merge_two_images_fun(foregrond_image_path = bg_remove, background_image_path = blurred_bg, system_file_path = system_file_path)
    combined_image = cv2.imread(combined_image_path)
    save_to_final_folder(system_file_path, combined_image)
    return system_file_path