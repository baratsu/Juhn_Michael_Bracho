import random
from datetime import datetime
from zoneinfo import ZoneInfo

import streamlit as st

st.set_page_config(
    page_title="Juhn Michael Bracho | Profile",
    page_icon="👋",
    layout="wide",
)

QUOTES = (
    "Small steps still move you forward.",
    "Curiosity turns ordinary days into new beginnings.",
    "Keep showing up; progress is built one try at a time.",
    "You do not need to know everything to begin.",
    "Make today a little better than yesterday.",
)


def time_based_greeting(now: datetime, name: str = "") -> str:
    if 5 <= now.hour < 12:
        greeting = "Good morning"
    elif 12 <= now.hour < 17:
        greeting = "Good afternoon"
    elif 17 <= now.hour < 22:
        greeting = "Good evening"
    else:
        greeting = "Hello, night owl"

    return f"{greeting}, {name}!" if name else f"{greeting}!"


def generate_quote() -> None:
    current_quote = st.session_state["profile_quote"]
    next_quotes = [quote for quote in QUOTES if quote != current_quote]
    st.session_state["profile_quote"] = random.choice(next_quotes)


theme_choice = st.radio("Appearance", ("🌙 Dark", "☀️ Light"), horizontal=True)
dark_mode = theme_choice.startswith("🌙")
theme_colors = {
    "background": (
        "radial-gradient(ellipse at 10% 12%, rgba(255, 122, 54, 0.13), transparent 30%),"
        "radial-gradient(ellipse at 90% 70%, rgba(126, 91, 255, 0.10), transparent 28%),"
        "#0b0d12"
        if dark_mode
        else "radial-gradient(ellipse at 10% 12%, #f5d6bd 0, transparent 30%),"
        "radial-gradient(ellipse at 90% 70%, #dfe6d7 0, transparent 28%),"
        "#f7f1e7"
    ),
    "text": "#f5f5f7" if dark_mode else "#24211f",
    "muted": "#b8b8c2" if dark_mode else "#625c58",
    "panel": "rgba(22, 24, 31, 0.88)" if dark_mode else "rgba(255, 255, 255, 0.86)",
    "border": "#292b34" if dark_mode else "#e5d7ca",
    "field": "#111319" if dark_mode else "#fffdfa",
    "tag": "#171920" if dark_mode else "#fff7ef",
    "tag_border": "#343640" if dark_mode else "#e8cdb8",
}

theme_css = """
    <style>
    .stApp {
        background: THEME_BACKGROUND;
    }
    .block-container {
        max-width: 1120px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    .stApp, .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp label {
        color: THEME_TEXT;
    }
    .intro {
        padding: 1rem 0;
        animation: rise-in 850ms cubic-bezier(0.2, 0.7, 0.2, 1) both;
    }
    .intro > p {
        color: THEME_MUTED;
        font-size: 1.08rem;
    }
    .typing-line {
        display: inline-block;
        max-width: 100%;
        overflow: hidden;
        border-right: 2px solid #ff8a45;
        white-space: nowrap;
        animation:
            typing-first 2.4s steps(47, end) 500ms both,
            cursor-blink 750ms step-end 3.4s infinite;
    }
    .typing-line-second {
        animation:
            typing-second 1.2s steps(22, end) 3s both,
            cursor-blink 750ms step-end 4.3s infinite;
    }
    @media (max-width: 640px) {
        .typing-line {
            font-size: 0.68rem;
        }
    }
    .welcome-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.55rem;
        padding: 0.45rem 0.75rem;
        border: 1px solid THEME_BORDER;
        border-radius: 999px;
        background: THEME_PANEL;
        color: THEME_TEXT;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .welcome-dot {
        width: 0.55rem;
        height: 0.55rem;
        border-radius: 50%;
        background: #ff8a45;
        box-shadow: 0 0 12px rgba(255, 138, 69, 0.8);
        animation: pulse 1.7s ease-in-out infinite;
    }
    .clock-label {
        color: #ff9a5c;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
    }
    .clock-time {
        margin: 0.4rem 0 0;
        color: THEME_TEXT;
        font-size: clamp(2rem, 5vw, 3rem);
        font-variant-numeric: tabular-nums;
        font-weight: 800;
        letter-spacing: -0.05em;
    }
    .clock-date, .clock-note {
        color: THEME_MUTED;
        font-size: 0.9rem;
    }
    .quote-text {
        min-height: 3.2rem;
        margin: 0.6rem 0 1rem;
        color: THEME_TEXT;
        font-size: 1.2rem;
        font-weight: 600;
        line-height: 1.5;
    }
    @keyframes rise-in {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulse {
        50% { opacity: 0.55; transform: scale(0.78); }
    }
    @keyframes typing-first {
        from { width: 0; }
        to { width: 47ch; }
    }
    @keyframes typing-second {
        from { width: 0; }
        to { width: 22ch; }
    }
    @keyframes cursor-blink {
        50% { border-color: transparent; }
    }
    .eyebrow, .section-label {
        color: #ff9a5c;
        font-size: 0.76rem;
        font-weight: 700;
        letter-spacing: 0.18em;
        text-transform: uppercase;
    }
    .intro h1 {
        margin: 0.7rem 0;
        color: THEME_TEXT;
        font-size: clamp(3rem, 7vw, 5.3rem);
        font-weight: 800;
        letter-spacing: -0.07em;
        line-height: 0.98;
    }
    .intro h1 span {
        color: #ff8a45;
    }
    [data-testid="stImage"] {
        animation: rise-in 900ms 120ms cubic-bezier(0.2, 0.7, 0.2, 1) both;
    }
    [data-testid="stImage"] img {
        border: 2px solid rgba(255, 138, 69, 0.75);
        border-radius: 24px;
        box-shadow: 0 20px 60px rgba(255, 111, 44, 0.14);
    }
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-color: THEME_BORDER;
        border-radius: 20px;
        background: THEME_PANEL;
    }
    [data-testid="stForm"] {
        padding: 1.2rem;
        border: 1px solid THEME_BORDER;
        border-radius: 20px;
        background: THEME_PANEL;
    }
    [data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea {
        color: THEME_TEXT;
        border-color: THEME_BORDER;
        background: THEME_FIELD;
    }
    .stButton button, [data-testid="stFormSubmitButton"] button {
        border: 0;
        border-radius: 12px;
        background: #ff8a45;
        color: #17120f;
        font-weight: 700;
    }
    .stButton button:hover, [data-testid="stFormSubmitButton"] button:hover {
        border: 0;
        background: #ffab73;
        color: #17120f;
    }
    .tag-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.65rem;
        margin: 1.2rem 0 0;
    }
    .tag {
        padding: 0.48rem 0.78rem;
        border: 1px solid THEME_TAG_BORDER;
        border-radius: 999px;
        background: THEME_TAG;
        color: THEME_TEXT;
        font-size: 0.86rem;
    }
    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after {
            animation-duration: 0.01ms !important;
            animation-iteration-count: 1 !important;
            scroll-behavior: auto !important;
        }
    }
    </style>
"""
for token, color in (
    ("THEME_BACKGROUND", theme_colors["background"]),
    ("THEME_TEXT", theme_colors["text"]),
    ("THEME_MUTED", theme_colors["muted"]),
    ("THEME_PANEL", theme_colors["panel"]),
    ("THEME_BORDER", theme_colors["border"]),
    ("THEME_FIELD", theme_colors["field"]),
    ("THEME_TAG_BORDER", theme_colors["tag_border"]),
    ("THEME_TAG", theme_colors["tag"]),
):
    theme_css = theme_css.replace(token, color)
st.markdown(theme_css, unsafe_allow_html=True)

intro_column, image_column = st.columns([1.35, 0.85], vertical_alignment="center")

with intro_column:
    st.markdown(
        """
        <div class="intro">
            <div class="welcome-pill"><span class="welcome-dot"></span> WELCOME TO MY CORNER OF THE WEB</div>
            <div class="eyebrow">PERSONAL PROFILE &nbsp;·&nbsp; 01</div>
            <h1>Juhn Michael<br><span>Bracho.</span></h1>
            <p>
                <span class="typing-line">Learning, creating, and bringing ideas to life—</span><br>
                <span class="typing-line typing-line-second">one project at a time.</span>
            </p>
        </div>
        <div class="tag-row">
            <span class="tag">Curious mind</span>
            <span class="tag">Always learning</span>
            <span class="tag">Building with Streamlit</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

with image_column:
    st.image("pitsur.jpeg", use_container_width=True)

@st.fragment(run_every="1s")
def live_clock() -> None:
    now = datetime.now(ZoneInfo("Asia/Manila"))
    visitor_name = st.session_state.get("visitor_name", "")

    clock_column, greeting_column = st.columns([1, 1.2])
    with clock_column:
        with st.container(border=True):
            st.markdown(
                '<div class="clock-label">LIVE CLOCK · PHILIPPINE TIME</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="clock-time">{now.strftime("%I:%M:%S %p")}</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="clock-date">{now.strftime("%A, %B %d, %Y")}</div>',
                unsafe_allow_html=True,
            )
            st.markdown(
                '<div class="clock-note">Philippine Standard Time (UTC+08:00)</div>',
                unsafe_allow_html=True,
            )

    with greeting_column:
        with st.container(border=True):
            st.markdown('<div class="clock-label">A NOTE FOR YOU</div>', unsafe_allow_html=True)
            st.subheader(time_based_greeting(now, visitor_name))
            st.write("Hope your day is going well. Thanks for visiting my profile!")


live_clock()

st.markdown('<div class="section-label">01 / ABOUT ME</div>', unsafe_allow_html=True)
about_column, detail_column = st.columns([1.25, 0.75])

with about_column:
    with st.container(border=True):
        st.subheader("Hey, glad you're here.")
        st.write(
            "I'm Juhn Michael Bracho. This is my first Streamlit web application, "
            "and a little space to introduce myself. Thanks for stopping by."
        )

with detail_column:
    with st.container(border=True):
        st.subheader("Currently")
        st.write("Exploring Streamlit and learning by building.")

st.markdown('<div class="section-label">02 / SAY HELLO</div>', unsafe_allow_html=True)
st.write("Drop your name below for a personal welcome.")

with st.form("visitor_greeting"):
    name = st.text_input("Your name", placeholder="Type your name here")
    submitted = st.form_submit_button("Send a hello  →", type="primary")

if submitted:
    if name.strip():
        st.session_state["visitor_name"] = name.strip()
        st.success(f"Nice to meet you, {name.strip()}! Thanks for stopping by.")
        st.balloons()
    else:
        st.warning("Add your name first, then send your hello.")

st.markdown('<div class="section-label">03 / A LITTLE INSPIRATION</div>', unsafe_allow_html=True)
if "profile_quote" not in st.session_state:
    st.session_state["profile_quote"] = random.choice(QUOTES)

with st.container(border=True):
    quote_column, button_column = st.columns([1.6, 0.6], vertical_alignment="center")
    with quote_column:
        st.markdown('<div class="clock-label">YOUR RANDOM REMINDER</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="quote-text">“{st.session_state["profile_quote"]}”</div>',
            unsafe_allow_html=True,
        )
    with button_column:
        st.button(
            "Inspire me  ↻",
            type="primary",
            on_click=generate_quote,
            key="generate_quote_button",
        )

st.markdown('<div class="section-label">04 / FAQ</div>', unsafe_allow_html=True)
st.subheader("A few quick answers")

faq_items = (
    (
        "What is this page?",
        "It's my personal profile and my first Streamlit web application.",
    ),
    (
        "What am I learning right now?",
        "I'm exploring Streamlit and learning by building.",
    ),
    (
        "What timezone does the clock use?",
        "The live clock and personalized greeting use Philippine time (Asia/Manila, UTC+08:00).",
    ),
    (
        "Is my feedback saved?",
        "Feedback is kept only for the current app session. It isn't sent to an external service or saved permanently.",
    ),
    (
        "Can I change how the profile looks?",
        "Yes. Use the Appearance control at the top of the page to switch between dark and light themes.",
    ),
)

for question, answer in faq_items:
    with st.expander(question):
        st.write(answer)

st.markdown('<div class="section-label">05 / VISITOR FEEDBACK</div>', unsafe_allow_html=True)
st.caption("Your feedback is kept only for this app session; it is not sent to an external service.")

if "visitor_feedback" not in st.session_state:
    st.session_state["visitor_feedback"] = []

with st.form("visitor_feedback_form", clear_on_submit=True):
    rating = st.slider("How was your visit?", min_value=1, max_value=5, value=4)
    feedback = st.text_area(
        "What could make this profile better?",
        placeholder="Share a quick thought...",
        max_chars=500,
    )
    feedback_submitted = st.form_submit_button("Submit feedback  →", type="primary")

if feedback_submitted:
    if feedback.strip():
        st.session_state["visitor_feedback"].append(
            {"rating": rating, "comment": feedback.strip()}
        )
        st.success("Thanks for the feedback! Your response is saved for this session.")
    else:
        st.warning("Write a quick comment before submitting your feedback.")

st.markdown(
    '<div style="text-align:center; color:#85858f; padding-top:2rem;">'
    "MADE WITH STREAMLIT &nbsp;·&nbsp; JUHN MICHAEL BRACHO"
    "</div>",
    unsafe_allow_html=True,
)