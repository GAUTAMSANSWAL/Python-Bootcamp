import qrcode

text = input("enter the text you want to convert into the qr code")
filename = input("enter the name for the qr code image file without extention")
filename = filename + ".png"

img = qrcode.make(text)
img.save(filename)