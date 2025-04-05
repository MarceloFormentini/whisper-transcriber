import whisper
import os

def transcribe_audio(file_path: str, model_size="large") -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    print(f"Carregando modelo Whisper [{model_size}]...")
    model = whisper.load_model(model_size)
    print("Modelo carregado. Iniciando transcrição...")

    abs_path = os.path.abspath(file_path)
    print("Caminho absoluto do áudio:", abs_path)

    result = model.transcribe(abs_path, language="Portuguese")
    return result["text"]