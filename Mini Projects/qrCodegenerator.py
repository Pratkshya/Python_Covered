import qrcode

getData = input("Enter the text or URL you want to create: ").strip()
fileName = input("Enter the filename: ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(getData)
image = qr.make_image(fill_color='black', black_color='white')
image.save(fileName)
print(f"QR Code saved as a {fileName}")

