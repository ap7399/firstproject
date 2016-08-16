from PIL import Image
im = Image.open("harry.jpg")
#pix = im.load()
im.size 
#print(im.size)
#print pix[200, 200]
#im.mode()
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

pixels = list(im.getdata())

#print(pixels)
new_pixels = []

for i in pixels:
	total_rgb= i[0] + i[1] + i[2]
	if total_rgb<182:
		new_pixels.append(darkBlue)
	elif 182<total_rgb<364:
		new_pixels.append(red)
	elif 364<total_rgb<546:
		new_pixels.append(lightBlue)
	else:
		new_pixels.append(yellow)
new=Image.new("RGB", (237,212))
new.putdata(new_pixels)
new.show()
new.save("harrycon.jpg", "jpeg")

#need to create an empty space to put an append in, image being transformed into a list, evaluated by the if statement,
