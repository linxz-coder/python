from PIL import Image, UnidentifiedImageError
import os
import sys

# 1.get the input and output folder from terminal
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# test the command
# print(image_folder, output_folder)

# 2. if the new folder does not exist, create one
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

# 3. loop throuth the input folder
for filename in os.listdir(image_folder):
	# 4. if images cannot be identified, continue the loop
	try:
		img = Image.open(f'{image_folder}{filename}')
		change_state = True
	except UnidentifiedImageError:
		print('未修改1张照片')
		continue
		# change_state = False
	img.thumbnail((200, 200))
	# 5. if change_state, save the image; else, overlook it
	if change_state:
		split_name = os.path.splitext(filename)
		# print(split_name[0])
		img.save(f'{output_folder}{split_name[0]}_resize{split_name[1]}')
		# img.save(output_folder + "resize_" + filename)
		print('已修改1张照片')