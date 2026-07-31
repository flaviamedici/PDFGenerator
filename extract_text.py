import fitz

with fitz.open("students.pdf") as pdf:
    text = ''
    for page in pdf:
        #if you need to print only one single page
        #page1 = pdf[0].get_text()

        text = text + page.get_text()
        print(text)