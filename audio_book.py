import pyttsx3
import PyPDF2
book = open('b.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page=pdfReader.getPage(11)
txt = page.extractText()
speaker.say(txt)
speaker.runAndWait()
