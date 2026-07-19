import cv2
from PIL import Image
from PIL.ExifTags import TAGS 

# / metadata time
def get_photo_info (path):
    image = Image.open(path) #holds the photo itself, path was only tthere to tell what image.open(path) was suppose to do.
    meta_data = image._getexif() 
    #loop time , it's the mechanism for reaching each individual pair, one at a time, so you can convert the tag ID into a readable name and print it clearly.
    if meta_data is None:
        print("No EXIF data found.")
        return
    for tag_id, value in meta_data.items(): 
        tag_name = TAGS.get(tag_id, tag_id) #this converts a number into its word
        return(tag_name, value)
get_photo_info("/Users/anisaraya/Desktop/repos/MLphoto/IMG_0179.JPG")

def get_sharpness_score(path): 
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    return(laplacian.var())
get_sharpness_score("/Users/anisaraya/Desktop/repos/MLphoto/IMG_0179.JPG")

filename = "IMG_0179.jpg"
if filename.lower().endswith((".jpg", ".jpeg", ".png", ".heic")):
    # run some tests