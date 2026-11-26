# Content Repurposing Agent

Paste one piece of long-form content and get five platform-ready formats instantly.  
Runs entirely on your machine using **Qwen** via **Ollama** + LangChain.

## Outputs
- Short summary
- LinkedIn post (150–250 words)
- Twitter / X thread (5–7 tweets)
- Email newsletter blurb (with CTA)
- Instagram caption (with hashtags)

## Requirements
- Python 3.10+
- [Ollama](https://ollama.com) installed and running

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
ollama pull qwen2.5:1.5b
```

## Run
```bash
streamlit run app.py
```
