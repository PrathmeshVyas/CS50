from PIL import Image, ImageFilter


b = Image.open('shiva.bmp')
a=b.filter(ImageFilter.BoxBlur(0))
a.save("out.bmp")

