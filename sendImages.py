from dotenv import load_dotenv
from collections import deque
import pandas as pd
import requests
import base64
import os


def send_img(img_path, img_name):
    load_dotenv()
    url = "https://api.imgbb.com/1/upload"
    apikey = os.getenv("API_KEY")

    # ENCODES THE IMG AS STRING IN BASE 64
    img_b64 = img_to_b64(img_path)

    # HEADERS THAT ARE SEND TO IMGDB
    # "expiration" : segs
    # 604800
    payload = {"key": apikey, "image": img_b64,
               "name": img_name, "expiration": 604800, }

    r = requests.post(url=url, data=payload)

    if (r.status_code == 200):
        dic_response = r.json()
        img_url = dic_response["data"]["image"]["url"]

        print(f"{img_name} UPLOADED SUCCESSFULLY!!!")
        return img_url
    else:
        print(r.text)

    return ""


def img_to_b64(img_full_path: str):
    try:
        with open(img_full_path, "rb") as f:
            img_bytes = f.read()
    except OSError as e:
        print("ERROR WHILE READING FILE")
        print(f"ERROR WAS {e}")

        return

    # ENCODES THE IMG AS STRING IN BASE 64
    base_64_img = base64.b64encode(img_bytes).decode("utf8")

    return base_64_img


def is_extension_valid(img_full_path: str, extensions=[]):
    ext_sep = img_full_path.rfind('.')

    if ext_sep >= 0:
        return img_full_path[ext_sep+1:] in extensions
    return False

def erase_extension(img_name):
    index = img_name.rfind(".")
    
    return (img_name[:index] if index >= 0 else  "")

def send_imgs(src_full_path: str, spreedsheat_full_path:str):
    valid_extensions = ['jpg', 'jpeg', 'png']

    for img_file in os.scandir(src_full_path):

        if is_extension_valid(img_file.name, valid_extensions):
            
            dic_of_img_urls = {}

            img_name_no_ext = erase_extension(img_file.name)
            img_url = send_img(img_file.path, img_name_no_ext);
            dic_of_img_urls[img_name_no_ext] = [img_url]

            print(f'\nFULL_PATH: {img_file.path}')
            print(f'URL: {img_url}\n')
            write_to_excel(dic_of_img_urls, spreedsheat_full_path, img_name_no_ext)
            


def create_table(dataframe, spreedsheat_full_path):
    writer = pd.ExcelWriter(path=spreedsheat_full_path, engine="openpyxl", mode="w")
    dataframe.to_excel(writer, sheet_name="Plan1",
                       startrow=0, header=False)
    writer.close()


def write_to_excel(dic: dict, spreedsheat_full_path:str, image_name:str):
    dataframe = pd.DataFrame(data=dic)
    dataframe = dataframe.transpose()

    # Check if the spread_sheet already exists
    if os.path.exists(spreedsheat_full_path) == False:
        create_table(dataframe=dataframe, spreedsheat_full_path=spreedsheat_full_path)
        return 
    
    writer = pd.ExcelWriter(
        path=spreedsheat_full_path, engine="openpyxl", mode="a", if_sheet_exists="overlay")
    dataframe.to_excel(writer, sheet_name="Plan1",
                       startrow=writer.sheets["Plan1"].max_row, header=False)
    writer.close()


def main():
    send_imgs('full_path_imgs', 'full_path_spread_sheet')


if __name__ == "__main__":
    main()
