# For You — V2

Multi-screen Streamlit appreciation/memory experience.

## Structure
- app.py
- requirements.txt
- README.md
- photos/

Put JPG, JPEG, PNG, or WEBP files into `photos/`. The Memories screen automatically displays them.

## Groq
The optional AI storyteller uses `openai/gpt-oss-120b`.

In Streamlit Cloud → Settings → Secrets:

```toml
GROQ_API_KEY = "your_key_here"
```

Never commit the real API key to GitHub.

## Deploy
Upload all files/folders to GitHub, create a Streamlit Cloud app using `app.py`, then add the secret above.
