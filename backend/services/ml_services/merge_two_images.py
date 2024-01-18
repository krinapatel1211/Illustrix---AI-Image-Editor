import cv2

from services.file import save_to_sub_folder
from config.settings import file_structure

def merge_two_images_fun(foregrond_image_path: str, background_image_path: str, system_file_path: str) -> str:
    foreground = cv2.imread(foregrond_image_path)
    fore_gray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)
    _, binary_mask = cv2.threshold(fore_gray, 1, 255, cv2.THRESH_BINARY)
    background = cv2.imread(background_image_path)
    background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))
    combined_image = background.copy()
    combined_image[ binary_mask > 0 ] = foreground[ binary_mask > 0 ]
    combined_image_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.USER_COMBINED_IMAGE_PATH + system_file_path.split("/")[-1]
    save_to_sub_folder(combined_image_path, combined_image)
    return combined_image_path