from rembg import remove
from PIL import Image

input_path = 'CL.jpg'
output_path = 'output.jpg' 

input =  Image.open(input_path)
output = remove(input)
output.save(output_path)
 