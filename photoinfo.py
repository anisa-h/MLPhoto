import cv2
import os 
import csv
import imagehash
from PIL import Image
from PIL.ExifTags import TAGS 

# / metadata time
def get_photo_info (path):
    image = Image.open(path) #holds the photo itself, path was only tthere to tell what image.open(path) was suppose to do.
    meta_data = image._getexif() 
    #loop time , it's the mechanism for reaching each individual pair, one at a time, so you can convert the tag ID into a readable name and print it clearly.
    result = {}

    if meta_data is None:
        print("No EXIF data found.")
        return
    for tag_id, value in meta_data.items(): 
        tag_name = TAGS.get(tag_id, tag_id) #this converts a number into its word
        if tag_name == "DateTimeOriginal":
            result["date"] = value
        if tag_name == "ExifImageWidth":
            result["width"] = value
        if tag_name == "ExifImageHeight":
            result["height"] = value
    
    return result 


def get_sharpness_score(path): 
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    return(laplacian.var())


def get_hash_score(path):
    score = imagehash.phash(Image.open(path))
    return score
#30+ means the photos are very unrelated, but single digts means its very likely a duplicate.

folder_path = "/Users/anisaraya/Desktop/repos/MLphoto"
all_photo_data=[]
for filename in os.listdir(folder_path):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".heic")):
        full_path = os.path.join(folder_path, filename)

        sharpness = get_sharpness_score(full_path)
        info = get_photo_info(full_path)
        scoreinfo = get_hash_score(full_path)
        row = {"filename": filename, "sharpness": sharpness, "hash": scoreinfo}
        row.update(info)
    
        all_photo_data.append(row)

with open("photos.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=all_photo_data[0].keys())
    writer.writeheader()
    writer.writerows(all_photo_data) 
#open this file, call it f while I'm using it, and when I'm done with everything inside this indented block, close the file automatically, even if something goes wrong.

print("done, wrote", len(all_photo_data), "rows")


#sliding scale for the the 
numbers = [3, 1, 2]
print(sorted(numbers))

sorted_photos = lambda timematters