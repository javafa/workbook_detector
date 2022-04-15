import fitz
import os


# 문제 pdf
content_dir = "./pdf/valid"
content_pdf_list = os.listdir(content_dir)

# 
matrix = fitz.Matrix(1.0, 1.0)

file_idx = 11

for file in content_pdf_list :
    if file.endswith(".pdf") :
        file_idx += 1
        file_name = f'val_{file_idx}'.zfill(3)
        
        doc = fitz.open(f'{content_dir}/{file}')
        for page in doc:
            pix = page.get_pixmap(matrix=matrix)
            page_number = f'{page.number}'.zfill(3)
            image_name = f'{file_name}_{page_number}.png'
            pix.save(f'{content_dir}/images/{image_name}')
            print("sliced ", image_name)