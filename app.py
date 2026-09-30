import os
import html
from pathlib import Path
import streamlit as st
from groq import Groq

st.set_page_config(page_title="For You 🤍", page_icon="🤍", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Inter:wght@400;500;600&display=swap');
html,body,[data-testid="stAppViewContainer"]{background:radial-gradient(circle at 15% 10%,rgba(224,185,143,.12),transparent 27%),radial-gradient(circle at 85% 75%,rgba(126,139,184,.10),transparent 30%),#08090d;color:#f5f1e9}
[data-testid="stHeader"]{background:transparent}.block-container{max-width:1050px;padding:1.8rem 1.2rem 5rem}
.nav{text-align:center;font:.68rem Inter,sans-serif;letter-spacing:.28em;text-transform:uppercase;color:#9e9a93;margin:1rem 0 2rem}
.hero{min-height:72vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.eyebrow,.kicker{color:#e5c6a6;font:500 .67rem Inter,sans-serif;text-transform:uppercase;letter-spacing:.28em}
.hero h1{font:500 clamp(4rem,11vw,8rem) "Cormorant Garamond",serif;line-height:.82;margin:.8rem 0 1.4rem;letter-spacing:-.045em}
.hero p,.story{max-width:720px;color:#c4c0b8;font:1rem/1.9 Inter,sans-serif}
.page{padding:3rem 0 1rem}.page h2{font:500 clamp(3rem,7vw,5.8rem) "Cormorant Garamond",serif;line-height:.9;margin:.6rem 0 1.5rem}
.story{font:1.45rem/1.55 "Cormorant Garamond",serif;color:#d9d4ca}
.quote{max-width:760px;margin:2.5rem auto;padding:1.8rem 2rem;border-left:2px solid #e5c6a6;background:rgba(255,255,255,.035);font:1.65rem/1.45 "Cormorant Garamond",serif;color:#eee9df}
.memory{border:1px solid rgba(255,255,255,.1);border-radius:22px;padding:1.5rem;background:linear-gradient(145deg,rgba(255,255,255,.06),rgba(255,255,255,.018));min-height:180px}
.memory b{font:500 1.55rem "Cormorant Garamond",serif}.memory p{font:.88rem/1.7 Inter,sans-serif;color:#aaa69f}
.final{min-height:70vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}
.final h2{font:500 clamp(3.5rem,9vw,7rem) "Cormorant Garamond",serif;line-height:.84}.final p{max-width:620px;color:#bdb8b0;font:.95rem/1.9 Inter,sans-serif}
.caption{text-align:center;color:#9f9b94;font:.8rem/1.6 Inter,sans-serif;margin-top:.8rem}
.stButton>button{border-radius:999px!important;border:1px solid rgba(229,198,166,.35)!important;background:rgba(229,198,166,.07)!important;color:#f4eee5!important;min-height:2.7rem!important}
.stButton>button:hover{background:rgba(229,198,166,.15)!important}
div[data-testid="stTextArea"] textarea{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);color:#fff;border-radius:15px}
.footer{text-align:center;color:#66635f;font:.7rem Inter,sans-serif;margin-top:4rem}
</style>
""", unsafe_allow_html=True)

pages = ["The Beginning","The First Day","The Change","The Memories","The Little Things","A Note","The Last Page"]
if "page" not in st.session_state: st.session_state.page = 0

def go(i):
    st.session_state.page = i
    st.rerun()

if st.session_state.page > 0:
    st.markdown(f'<div class="nav">{st.session_state.page+1:02d} / {len(pages):02d} · {html.escape(pages[st.session_state.page])}</div>', unsafe_allow_html=True)
    a,b=st.columns(2)
    with a:
        if st.button("← Previous",use_container_width=True): go(st.session_state.page-1)
    with b:
        if st.session_state.page < len(pages)-1 and st.button("Next →",use_container_width=True): go(st.session_state.page+1)

if st.session_state.page == 0:
    st.markdown("""<div class="hero"><div class="eyebrow">A small place made with care</div><h1>For You.</h1><p>Not a perfect story. Not a collection of big promises. Just a few memories, changes, and things I never knew how to say properly.</p></div>""",unsafe_allow_html=True)
    c1,c2,c3=st.columns(3)
    with c2:
        if st.button("Begin the story →",use_container_width=True): go(1)
    st.markdown('<div class="caption">Take your time. There is no rush.</div>',unsafe_allow_html=True)

elif st.session_state.page == 1:
    st.markdown("""<div class="page"><div class="kicker">01 — The first day</div><h2>The girl I first met.</h2><div class="story">I still remember the first time I started talking to you. I was asking you about something ordinary, but there was something about you that stood out to me.<br><br>You were quiet. Shy. Innocent in a way I noticed before I even knew how important you would become to me.<br><br>I didn't know that a simple conversation would eventually become a friendship I would remember this much.</div></div><div class="quote">Some beginnings are small. You only understand their importance later.</div>""",unsafe_allow_html=True)

elif st.session_state.page == 2:
    st.markdown("""<div class="page"><div class="kicker">02 — The change</div><h2>Somewhere along the way, I changed too.</h2><div class="story">I realized that the version of me from before wasn't the version I wanted to bring into this friendship.<br><br>So I worked on myself. I tried to be less angry, less rude, and more patient. I tried to become someone who could actually be a good friend to you.<br><br>Not because you demanded it. Because you mattered enough for me to want to show up differently.</div></div><div class="quote">Sometimes someone doesn't ask you to change. Caring about them makes you want to become better on your own.</div>""",unsafe_allow_html=True)

elif st.session_state.page == 3:
    st.markdown("""<div class="page"><div class="kicker">03 — The memories</div><h2>The days I keep.</h2><div class="story">The last day we spent together is one I remember especially clearly: making videos, rushing around together, doing random things, and somehow making an ordinary day feel amazing.</div></div>""",unsafe_allow_html=True)
    photo_dir=Path(__file__).parent/"photos"
    imgs=sorted([p for p in photo_dir.iterdir() if p.suffix.lower() in {".jpg",".jpeg",".png",".webp"}]) if photo_dir.exists() else []
    if imgs:
        for p in imgs:
            st.image(str(p),use_container_width=True)
            st.markdown(f'<div class="caption">{html.escape(p.stem.replace("_"," "))}</div>',unsafe_allow_html=True)
    else:
        st.info("Your gallery is ready. Put JPG, JPEG, PNG, or WEBP files inside the photos folder and upload that folder to GitHub.")
        cols=st.columns(3)
        for col,(n,t,b) in zip(cols,[("01","The first conversation","A small beginning that became meaningful."),("02","The time we spent","Ordinary days that became memories."),("03","That last day","Videos, rushing around, laughing, and being together.")]):
            with col:
                st.markdown(f'<div class="memory"><div class="kicker">{n}</div><b>{t}</b><p>{b}</p></div>',unsafe_allow_html=True)

elif st.session_state.page == 4:
    st.markdown("""<div class="page"><div class="kicker">04 — The little things</div><h2>You probably never noticed.</h2><div class="story">There were moments when I tried to control my anger and put my rudeness aside. There were moments when I felt ignored or lost some of my confidence. And there was time and effort I wouldn't normally give so easily.<br><br>I don't put those things here so you owe me anything. They are simply part of what this friendship meant to me.</div></div>""",unsafe_allow_html=True)
    a,b=st.columns(2)
    with a: st.markdown('<div class="memory"><div class="kicker">Something I appreciate</div><b>Your existence.</b><p>Not something you have to prove. Just you being part of my days.</p></div>',unsafe_allow_html=True)
    with b: st.markdown('<div class="memory"><div class="kicker">Something I remember</div><b>The person I first met.</b><p>The shy, quiet beginning that I still remember.</p></div>',unsafe_allow_html=True)

elif st.session_state.page == 5:
    st.markdown("""<div class="page"><div class="kicker">05 — A hidden storyteller</div><h2>Give me a memory.</h2><div class="story">This is the only AI-powered part of the experience. Write a real memory in your own words and the AI will turn it into a short, warm note.</div></div>""",unsafe_allow_html=True)
    raw=st.text_area("Your memory",placeholder="Example: We kept making videos on the last day and couldn't stop laughing...",height=160,label_visibility="collapsed")
    if st.button("Turn it into a little note →"):
        key=st.secrets.get("GROQ_API_KEY",os.getenv("GROQ_API_KEY",""))
        if not key: st.warning("Groq is not connected. Add GROQ_API_KEY in Streamlit Secrets.")
        elif not raw.strip(): st.info("Write a memory first.")
        else:
            try:
                client=Groq(api_key=key)
                prompt=f"""Turn the following real memory into a short, sincere appreciation note. Do not invent facts. Do not make it romantic, sexual, possessive, manipulative, or guilt-inducing. Keep the user's meaning and use simple natural English. 80-120 words.\n\nMemory:\n{raw.strip()}"""
                with st.spinner("Writing..."):
                    r=client.chat.completions.create(model="openai/gpt-oss-120b",messages=[{"role":"user","content":prompt}],temperature=.7,max_tokens=220)
                st.markdown(f'<div class="quote">{html.escape(r.choices[0].message.content.strip())}</div>',unsafe_allow_html=True)
            except Exception as e: st.error(f"Groq request failed: {e}")

elif st.session_state.page == 6:
    st.markdown("""<div class="final"><div class="kicker">06 — The last page</div><h2>You mattered.<br>And you still do.</h2><p>I didn't make this to ask anything from you. I just wanted you to have one place where you could see how much this friendship has meant to me.</p><p style="font:1.7rem 'Cormorant Garamond',serif;color:#e8e1d8;">You became one of the most important people in my life.</p><p>Thank you for being part of my story. 🤍</p></div>""",unsafe_allow_html=True)

st.markdown('<div class="footer">Made as a memory, not a measurement.</div>',unsafe_allow_html=True)
