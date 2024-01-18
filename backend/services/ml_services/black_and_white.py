import cv2

from services.file import save_to_final_folder, save_to_sub_folder, create_copy_image, check_copy_file_exist, delete_copy_file, revert_operation
from config.settings import file_structure

def black_and_white_fun(file_name: str, system_file_path: str, save: int, revert: int) -> str:
    black_and_white_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.BLACKA_AND_WHITE_PATH + system_file_path.split("/")[-1]
    operation_file_path = check_copy_file_exist(original_path = system_file_path, sub_path = black_and_white_path, file_name = file_name)
    image = cv2.imread(operation_file_path, cv2.IMREAD_GRAYSCALE)
    if operation_file_path == system_file_path:
        create_copy_image(from_path = system_file_path, to_path = black_and_white_path, file_name = file_name)
    save_to_sub_folder(black_and_white_path, image)
    save_to_final_folder(system_file_path, image)
    if save == 1:
        delete_copy_file(sub_path = black_and_white_path, file_name = file_name)
    if revert == 1:
        revert_operation(original_path = system_file_path, sub_path = black_and_white_path, file_name = file_name)
    return system_file_path