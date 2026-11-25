from PIL import Image

image = Image.new("RGB", (600, 400), "lightblue")
image.save("my_second_image.png")

print("My second image is ready!")
