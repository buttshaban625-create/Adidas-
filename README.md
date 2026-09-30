<img width="1080" height="1875" alt="IMG_20260929_234845" src="https://github.com/user-attachments/assets/5d324f11-6b30-49f6-90fb-c009e3632c6b" />
<img width="720" height="1280" alt="IMG-20260709-WA0157" src="https://github.com/user-attachments/assets/d7cf6029-8a4e-46ae-897b-aac11c6eb082" />
<img width="943" height="1600" alt="IMG-20260809-WA0000" src="https://github.com/user-attachments/assets/22e0d609-fd77-42df-b345-926671a2ff39" />



Uploading VID-20260709-WA0291.mp4…



https://github.com/user-attachments/assets/5e78753a-afae-4f29-b29b-ba70b1847cd5

<img width="943" height="1600" alt="IMG-20260809-WA0000" src="https://github.com/user-attachments/assets/341984a4-9bbf-42d6-aee7-2e7733f206da" />


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
