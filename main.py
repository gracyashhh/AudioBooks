import pdfplumber
import pyttsx3 as speech
pdf = pdfplumber.open('half.pdf')
pages=pdf.pages[16:]
speaker=speech.init()
for i,pg in enumerate(pages):
    text = pages[i].extract_text()
    speaker.say(text)
    speaker.runAndWait()
pdf.close()
