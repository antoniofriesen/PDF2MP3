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
    # Determine the number of characters to use for the progress bar
    total_chars = len(text)
    chunk_size = 100  # Number of characters to process in each iteration
    num_chunks = total_chars // chunk_size

    # Split text into chunks and process each chunk
    with open(output_path, 'wb') as f:
        for i in tqdm(range(num_chunks + 1), desc="Converting text to audio", unit='chunk'):
            start = i * chunk_size
            end = (i + 1) * chunk_size
            chunk = text[start:end]
            tts = gTTS(chunk)
            tts.write_to_fp(f)

def pdf_to_audio(pdf_path, output_path):
    text = extract_text_from_pdf(pdf_path)
    text_to_audio(text, output_path)

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    output_path = input("Enter the desired path for the output MP3 file (including filename with '.mp3' extension): ")
    print("Initialising ... done!")
    print("Executing the program!")
    pdf_to_audio(pdf_path, output_path)
    print("Conversion completed.")
