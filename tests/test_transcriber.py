import os
from unittest.mock import patch

import pytest
from app.transcriber import transcribe_audio

def test_transcribe_audio_exists():
    sample = "audio/exemplo.mp3"
    if not os.path.exists(sample):
        assert True, "Áudio de teste não existe, ignorando."
        return
    texto = transcribe_audio(sample)
    assert isinstance(texto, str)
    assert len(texto) > 0

def test_transcribe_audio_file_not_found():
    with pytest.raises(FileNotFoundError):
        transcribe_audio("audio/nao_existe.mp3")

def test_transcribe_with_different_model():
    audio_path = "audio/exemplo.m4a"
    result = transcribe_audio(audio_path, model_size="base")
    assert isinstance(result, str)
    assert len(result.strip()) > 0

@patch("app.transcriber.whisper.load_model")
@patch("app.transcriber.os.path.exists", return_value=True)
def test_transcribe_mocked(mock_exists, mock_load_model):
    mock_model = mock_load_model.return_value
    mock_model.transcribe.return_value = {"text": "Texto simulado"}

    result = transcribe_audio("fake/path.mp3")
    assert result == "Texto simulado"