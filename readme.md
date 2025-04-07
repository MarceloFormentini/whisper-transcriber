# Whisper Transcriber

![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/github/license/seu-usuario/whisper-transcriber)
![Build](https://img.shields.io/badge/build-passing-brightgreen)

Ferramenta simples para transcrição de áudios usando o modelo Whisper da OpenAI.

## 🚀 Como usar

1. Crie um ambiente virtual:
```bash
python -m venv .venv
```

2. Ative o ambiente:
- Linux/macOS:
  ```bash
  source .venv/bin/activate
  ```
- Windows:
  ```bash
  .venv\Scripts\activate
  ```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Coloque um arquivo `.mp3` em `audio/` e execute:
```bash
python main.py
```

A transcrição será salva na pasta `transcriptions/`.

## 🧠 Tecnologias
- Python 3.10
- Whisper (OpenAI)
- PyTorch

## 🐳 Executar com Docker

```bash
docker-compose up --build
```

## 🧪 Rodar testes
```bash
pytest
```

## 📁 Estrutura
```
whisper-transcriber/
├── app/
│   ├── __init__.py
│   ├── transcriber.py      # Código principal de transcrição
│   └── utils.py            # Funções auxiliares (ex: validação de arquivos)
├── tests/
│   └── test_transcriber.py # Teste automatizados
├── audio/                  # Pasta para armazenar os áudios
├── transcriptions/         # Saída das transcrições
├── requirements.txt        # Dependências
├── README.md               # Descrição do projeto
└── main.py                 # Script principal de execução
```

## 📌 Observações
- O modelo padrão é `base`, mas pode ser alterado para `small`, `medium` ou `large` no `transcribe_audio`.
- Suporta `.mp3`, `.wav`, `.m4a` etc.
- O diretório `audio/` deve conter os arquivos que deseja transcrever.

## 📜 Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.