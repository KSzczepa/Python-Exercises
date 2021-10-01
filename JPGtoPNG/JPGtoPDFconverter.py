import sys
import os
from PIL import Image
from pathlib import Path


# variables
parent_dir = r'D:\Dokumenty\Udemy_Courses\Python_Scripting\Image_processing\images'
mode = 0o666


def replaceSuffix(file_name):
    new_name = Path(file_name)
    #filename_wo_ext = new_name.with_suffix('')
    filename_replace_ext = new_name.with_suffix('.png')
    return filename_replace_ext

# convert images to png
def convertJPGtoPDF(jpg_image, img_name_jpg, final_dir):
    image_to_conv = Image.open(jpg_image)
    img = image_to_conv.convert('RGB')
    img_name_pdf = replaceSuffix(img_name_jpg)
    new_dir = os.path.join(final_dir, img_name_pdf)
    img.save(new_dir, 'png')



# grab first and second argument
jpg_dir = sys.argv[1]
jpg_dir_path = os.path.join(parent_dir, jpg_dir)
if not os.path.exists(jpg_dir_path):
    os.mkdir(jpg_dir_path, mode)


# check if new\ exist, and if not, create it
try:
    pdf_dir = sys.argv[2]
except IndexError:
    pdf_dir = 'NewPDF'

# make a full path
pdf_dir_path = os.path.join(parent_dir, pdf_dir)

# create folder if not exist
if not os.path.exists(pdf_dir_path):
    os.mkdir(pdf_dir_path, mode)


# loop through Pokedex folder
obj = os.scandir(jpg_dir_path)
for fname in obj:
    jpg_file = os.path.join(jpg_dir_path, fname)

    if fname.is_dir() or fname.is_file():
        filename = fname.name
        convertJPGtoPDF(jpg_file, filename, pdf_dir_path)


#easier way
# img = Image.open(f'{image_folder}{file_name}')
# cleam_name = os.path.splitext(file_name)[0]
# img.save(f'{output_folder}{cleam_name}.png', 'png')

