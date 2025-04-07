import whisper
import os
import torch
import tempfile
import shutil
from pydub import AudioSegment
from whisper.utils import get_writer
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

MODEL_NAME = 'large'
LANGUAGE = 'portuguese'

model = whisper.load_model(
    MODEL_NAME,
    device="cuda" if torch.cuda.is_available() else "cpu"
)

# transcreve pequenos trechos de áudio
def transcribe_segment(audio_path: str):
    result = model.transcribe(audio_path, language=LANGUAGE, beam_size=5, best_of=5)
    return result["text"]

# corrige e organiza frases de transcrição
def post_process(text: str) -> str:
    sentences = sent_tokenize(text, language=LANGUAGE)
    return " ".join(sentence.strip().capitalize() for sentence in sentences)

#divide áudio longo em segmentos de 60 segundos
def split_audio(file_path: str, segment_lenth: int = 60):
    audio = AudioSegment.from_file(file_path)
    duration = len(audio) // 1000
    segments = []
    temp_dir = tempfile.mkdtemp()

    for i in range(0, duration, segment_lenth):
        segment_path = os.path.join(temp_dir, f"segment_{i}.mp3")
        segment = audio[i * 1000:(i + segment_lenth) * 1000]
        segment.export(segment_path, format="mp3")
        segments.append(segment_path)

    return segments, temp_dir

def transcribe_audio(file_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    print("Modelo carregado. Iniciando transcrição...")
    segments, temp_dir = split_audio(file_path)
    full_text = ""

    for segment in segments:
        print(f"Transcrevendo: {os.path.basename(segment)}")
        try:
            segment_text = transcribe_segment(segment)
            full_text += segment_text + " "
        except Exception as e:
            print(f"Erro ao transcrever {segment}: {e}")

    shutil.rmtree(temp_dir)
    text = post_process(full_text)

    print(f"transcriptions/{os.path.splitext(os.path.basename(file_path))[0]}.txt")
    os.makedirs("transcriptions", exist_ok=True)
    with open(
        f"transcriptions/{os.path.splitext(os.path.basename(file_path))[0]}.txt", 
        "w", encoding="utf-8") as f:
        f.write(text)