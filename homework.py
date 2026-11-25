import qrcode

data = "Hello! I created this QR code using Python."
image = qrcode.make(data)
image.save("my_qrcode.png")

print("QR code created successfully!")
