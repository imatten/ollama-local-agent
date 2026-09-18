# Local AI Agent Playground

Run LLMs locally via Ollama, on CPU (no GPU needed). 

## Quick Start

```bash
make up      # Start Ollama + web UI
make down    # Stop everything
make logs    # View logs
```

- **Chat UI:** http://localhost:3000
- **Ollama API:** http://localhost:11434

## Pulling a model

```bash
make pull MODEL=qwen2.5:3b
```

Good small models for CPU-only laptops:

| Model | Size | Notes |
|-------|------|-------|
| `qwen2.5:3b` | ~2GB | fast, solid all-rounder |
| `llama3.2:3b` | ~2GB | fast, good for tool-calling |
| `qwen2.5:7b` | ~4.5GB | slower, smarter |

Then select it in the web UI, or call the API directly:

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "qwen2.5:3b",
  "prompt": "Why is the sky blue?"
}'
```

## Volumes

| Volume | Purpose |
|--------|---------|
| `./ollama_data` | pulled models + Ollama state |
| `./webui_data` | web UI settings/chat history |
