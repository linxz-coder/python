import sys
import os
from PIL import Image

# target: create a new folder to let Pokedex convert to png and store it to the new folder

# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

# check is new/ exists, if not create
if not os.path.exists(output_folder):
	os.makedirs(output_folder)
# os.path
# 

# loop through Pokedex,
for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	#删除掉jpeg的后缀
	clean_name = os.path.splitext(filename)[0]
	# print(clean_name)
	img.save(f'{output_folder}{clean_name}.png', 'png')
	print('all done!')

# convert images to png
# save to the new folder