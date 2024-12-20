import json
import os
import zipfile

with zipfile.ZipFile("image_info_test2017.zip", 'r') as zip_ref:
    zip_ref.extractall("image_info_test2017")

json_file_path = os.path.join("image_info_test2017", "annotations", "image_info_test-dev2017.json")

with open(json_file_path, 'r') as file:
    data = json.load(file)

images = data["images"]
num_images = len(images)
print(f"Number of images: {num_images}")

categories = data["categories"]
num_categories = len(categories)
print(f"Number of categories: {num_categories}")

for image in images:
    if image["file_name"] == "000000000001.jpg":
        print(f"URL: {image['coco_url']}")
        print(f"Height: {image['height']}")
        print(f"Width: {image['width']}")
        print(f"ID: {image['id']}")
        break

max_image = max(images, key=lambda x: int(x["file_name"].split('.')[0]))
print(f"Image with the highest number: {max_image['file_name']}")
