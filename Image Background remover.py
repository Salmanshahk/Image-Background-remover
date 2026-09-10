#Before run the script user need to install rembg package
# Command is pip install "rembg[cpu]" - for CPU installation  - library
#pip install "rembg[gpu,cli]"  - for library + cli
#pip install "rembg[gpu]" # for library - for GPU installation - library
#pip install "rembg[gpu,cli]" # for library + cli


from rembg import remove
from PIL import Image

# Path to input image
input_path = ''

#Load the image
input_image = Image.open(input_path)

#Remove Background
output_image = remove(input_image)

#Save the result with transparency
output_path = ''
output_image.save(output_image)

#Done

print(f"Background removed! Saved to: {output_path} successfully")