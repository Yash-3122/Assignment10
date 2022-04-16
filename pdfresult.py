
## 20CE112 Yash Patel
## Github Repository Link
## https://github.com/Yash-3122/Assignment10
## Practical 10- AIM: Generate PDF file of your 3rd Semester Mark-sheet

from PIL import Image

# Path for your image where it is
image_1 = Image.open(r"C:\Users\Dell\Pictures\New folder (3)\sem3Result.png")

# Converting it into pdf
im_1 = image_1.convert('RGB')

# Path where your PDF file will bw saved
im_1.save(r"C:\Users\Dell\Pictures\New folder (3)\sem3Resultusingpython.pdf")
print("pdf file of sem-3 result is successfully created from png image ")