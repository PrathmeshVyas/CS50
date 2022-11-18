import os
import qrcode

img = qrcode.make("https://github.com/Prathmeshvyas")
img.save("qr.png", "PNG")
os.system("open qr.png")