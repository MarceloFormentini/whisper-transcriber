# main.py
import os
import time
from app.transcriber import transcribe_audio

AUDIO_FILE = "./audio/exemplo.m4a"
OUTPUT_FILE = "transcriptions/exemplo.txt"

if __name__ == "__main__":
    # Grava o tempo inicial
    inicio = time.time()

    print("Transcrevendo:", AUDIO_FILE)
    text = transcribe_audio(AUDIO_FILE)

    os.makedirs("transcriptions", exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(text)

    # Grava o tempo final
    fim = time.time()
    tempo = fim - inicio
    print(f'Transcrição salva em: {OUTPUT_FILE}. Tempo de execucao: {tempo}')
