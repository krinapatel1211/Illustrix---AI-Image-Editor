from pydantic import BaseSettings

class DBSettings(BaseSettings):
    db_name: str = "illustrix"
    db_host: str = "localhost"
    db_port: int = 27017

db_settings = DBSettings()

class JWT(BaseSettings):
    JWT_Secret: str = "Femj4ul1V2Xk3A3Amy6w7cE9gVAdn96Y"
    JWT_Expiry_Time: int = 86400
    FMT: str = "%Y-%m-%d %H:%M:%S.%f"

jwt_setting = JWT()

class Constants(BaseSettings):
    SUCCESS_SIGNUP: str = "Successfully Singed Up!"
    SUCCESS_LOGIN: str = "Successfully Logged In!"
    INVALID_LOGIN: str = "Invalid Login!"
    ERROR: str = "Error Occured. Please Try again leter!"
    SUCCESSFULLY_PERFORMED: str = "Successfully Performed!"

constants = Constants()

class FileStructure(BaseSettings):
    SERVER_URL = "http://localhost:8000/"
    BASE_STRUCTURE: list = ["/upload", "/final", "/background_remove", "/background", "/background_blur", "/combined_image", "/flip_vertically", "/flip_horizontally", "/black_and_white", "/saturation", "/hue", "/contrast", "/brightness", "/sharpness", "/painting", "/sketching", "/cartoonification", "/image_super_resolution"]
    USER_DATA: str = "./static/user_data/"
    STATIC_FOLDER: str = "./static/"
    MODEL_FOLDER: str = "./services/ml_services/models/"
    FINAL_IMAGE_PATH: str = "/final"
    BACKGROUND_REMOVE_PATH: str = "/background_remove/"
    USER_BACKGROUND_PATH: str = "/background/"
    USER_BLURRED_BACKGROUND_PATH: str = "/background_blur/"
    UPLOAD_IMAGE_PATH: str = "/upload"
    USER_COMBINED_IMAGE_PATH: str = "/combined_image/"
    FLIP_VERTICAL_PATH: str = "/flip_vertically/"
    FLIP_HORIZONTAL_PATH: str = "/flip_horizontally/"
    BLACKA_AND_WHITE_PATH: str = "/black_and_white/"
    SATURATION_PATH: str = "/saturation/"
    HUE_PATH: str = "/hue/"
    CONTRAST_PATH: str = "/contrast/"
    BRIGHTNESS_PATH: str = "/brightness/"
    SHARPNESS_PATH: str = "/sharpness/"
    UPLOAD_PATH: str = "/upload/"
    PAINTING_PATH: str = "/painting/"
    SKETCHING_PATH: str = "/sketching/"
    CARTOONIFICATION_MODEL: str = "./services/ml_services/models/cartoonification_model"
    CARTOONNIFICATION_PATH: str = "/cartoonification/"
    COPY_FILE_SUFFIX: str = "_copy"
    IMAGE_SUPER_RESOLUTION_MODEL: str = "./services/ml_services/models/image_super_resolution/rrdn-C4-D3-G64-G064-T10-x2_best-val_generator_PSNR_Y_epoch009.hdf5"
    IMAGE_SUPER_RESOLUTION_PATH: str = "/image_super_resolution/"

file_structure = FileStructure()

class MLConstants(BaseSettings):
    BLUR_FACTOR: int = 25
    SHAPRNESS_FACTOR: int = 2
    IMAGE_SUER_RESOLUTION_SCALE: int = 2

ml_constants = MLConstants()