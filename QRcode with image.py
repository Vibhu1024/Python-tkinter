import qrcode
from PIL import Image

img_bg = Image.open('\Users\HP\PycharmProjects\pythonProject\qr_stephen-cook-xsoKzROUhRQ-unsplash.jpg')

qr = qrcode.QRCode(box_size=2)
qr.add_data('I am Lena')
qr.make()
img_qr = qr.make_image()

pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[1] - img_qr.size[1])

img_bg.paste(img_qr, pos)
img_bg.save('\Users\HP\PycharmProjects\pythonProject\qr_stephen-cook-xsoKzROUhRQ-unsplash.png')

face = Image.open('qr_stephen-cook-xsoKzROUhRQ-unsplash.jpg').crop((175, 90, 235, 150))

qr_big = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr_big.add_data('I am splash')
qr_big.make()
img_qr_big = qr_big.make_image().convert('RGB')

pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)

img_qr_big.paste(face, pos)
img_qr_big.save('/Users/HP/PycharmProjects/pythonProject/qr_stephen-cook-xsoKzROUhRQ-unsplash.png')