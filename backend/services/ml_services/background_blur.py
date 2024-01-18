import cv2

from config.settings import file_structure, ml_constants
from services.file import save_to_sub_folder

def background_blur_fun(file_name: str, system_file_path: str) -> str:
    foreground = cv2.imread(system_file_path, cv2.IMREAD_COLOR)
    bg_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.USER_BLURRED_BACKGROUND_PATH + system_file_path.split("/")[-1]
    original_img_path = system_file_path
    background = cv2.imread(original_img_path)
    background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))
    blurred_background = cv2.GaussianBlur(background, (ml_constants.BLUR_FACTOR, ml_constants.BLUR_FACTOR), 0)
    save_to_sub_folder(bg_path, blurred_background)
    return bg_path