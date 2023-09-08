import pyttsx3, PyPDF2, os
from pathlib import Path

# obtain file name from user
file_name = input("Enter file name: ")

# find and open the file
data_folder = Path("pdf_to_mp3_project/")
file_to_open = data_folder / file_name
try:
    pdfreader = PyPDF2.PdfFileReader(open(file_to_open, 'rb'))
except:
    print("File name not found.")

# set up voice
speaker = pyttsx3.init()
speaker.setProperty('rate', 115)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id) # 0 for male, 1 for female

# saved mp3 file name
save_to_name = file_name[:file_name.index('.')] + ".mp3"

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extract_text()
    clean_text = text.strip().replace('\n', ' ')

speaker.save_to_file(clean_text, save_to_name)
speaker.say("Your file is ready")
speaker.runAndWait()

speaker.stop()

src = "/Users/kevin/Documents/Python VS"
dst = "/Users/kevin/Documents/Python VS/pdf_to_mp3_project/saved"
src_path = os.path.join(src, save_to_name)
dst_path = os.path.join(dst, save_to_name)
os.rename(src_path, dst_path)
