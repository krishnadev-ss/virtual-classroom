# import module
from pdf2image import convert_from_path
# Store Pdf with convert_from_path function
images = convert_from_path('/home/krishnadev/Downloads/INTERMEDIATE.pdf')
output_folder = "/home/krishnadev/Downloads/new/"

for i in range(len(images)):
    # Save pages as images in the pdf
    images[i].save(output_folder + 'page' + str(i + 1) + '.jpg', 'JPEG')




