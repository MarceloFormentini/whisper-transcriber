# main.py
import os
import time
from app.transcriber import transcribe_audio

AUDIO_FILE = "./audio/exemplo.m4a"

if __name__ == "__main__":
    # Grava o tempo inicial
    inicio = time.time()

    transcribe_audio(AUDIO_FILE)

    # Grava o tempo final
    fim = time.time()
    tempo = fim - inicio
    print(f'Transcrição salva na pasta transcriptions. Tempo de execucao: {tempo}')
