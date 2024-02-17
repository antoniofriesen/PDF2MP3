import PyPDF2
from gtts import gTTS
import os
from tqdm import tqdm

def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in tqdm(range(len(reader.pages)), desc="Extracting text"):
            text += reader.pages[page_num].extract_text()
    return text

def text_to_audio(text, output_path):
    tts = gTTS(text)
    tts.save(output_path)

def pdf_to_audio(pdf_path, output_path):
    text = extract_text_from_pdf(pdf_path)
    text_to_audio(text, output_path)

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    output_path = input("Enter the desired path for the output MP3 file (including filename with '.mp3' extension): ")
    pdf_to_audio(pdf_path, output_path)
    print("Conversion complete.")

