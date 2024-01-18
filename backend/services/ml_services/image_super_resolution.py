import cv2
import numpy as np

from services.file import save_to_final_folder, save_to_sub_folder
from config.settings import file_structure, ml_constants



def image_super_resolution_fun(file_name: str, system_file_path: str) -> str:
    from ISR.models import RRDN
    rrdn  = RRDN(arch_params={'C':4, 'D':3, 'G':64, 'G0':64, 'T':10, 'x':ml_constants.IMAGE_SUER_RESOLUTION_SCALE}, patch_size=None)
    rrdn.model.load_weights(file_structure.IMAGE_SUPER_RESOLUTION_MODEL)
    super_resolution_path = file_structure.USER_DATA + system_file_path.split("/")[3] + file_structure.IMAGE_SUPER_RESOLUTION_PATH + system_file_path.split("/")[-1]
    img = cv2.imread(system_file_path)
    lr_img = np.array(img)
    super_resolution_image = rrdn.predict(lr_img)
    save_to_sub_folder(super_resolution_path, super_resolution_image)
    save_to_final_folder(system_file_path, super_resolution_image)
    del rrdn, RRDN