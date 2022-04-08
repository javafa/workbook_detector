import fitz

pdf  = fitz.open("./test.pdf")
cropbox =  pdf[0].CropBox
width = cropbox.width
height = cropbox.height

print(f'cropbox:{cropbox}')
print(f'w:{width}, h:{height}')