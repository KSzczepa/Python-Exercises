from PIL import Image, ImageFilter

#PIKACHU

#img = Image.open('./Pokedex/pikachu.jpg')

# print(img.format)
# print(img.size)
# print(img.mode)
#print(dir(img))

with Image.open('./Pokedex/pikachu.jpg') as img:
    filtered_img = img.filter(ImageFilter.BLUR)
    filtered_img.save("blur.png", 'png')

    filtered_img2 = img.filter(ImageFilter.SMOOTH)
    filtered_img2.save("smooth.png", 'png')

    filtered_img3 = img.convert('L')
    filtered_img3.save("grey.png", 'png')

    crooked = filtered_img3.rotate(90)
    crooked.save("crooked.png", 'png')

    resize = filtered_img3.resize((300, 300))
    resize.save("resized.png", 'png')

    box = (100, 100, 400, 400)
    region = filtered_img3.crop(box)
    region.save("cropped.png", 'png')

    #show image
    region.show()


with Image.open('./astro.jpg') as img_astro:
    print(img_astro.size)
    new_img_astro = img_astro.resize((400, 400))
    new_img_astro.save('thumbnail.jpg')

    # to make img ratio stay the same:
    #img.thimbnail((400,200))
    #img.save('thumbnail.jpg')