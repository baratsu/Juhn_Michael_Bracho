import streamlit as st

st.set_page_config(
    page_title="Juhn Michael Bracho | Profile",
    page_icon="👋",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(ellipse at 12% 8%, #dbeafe 0, transparent 34%),
            radial-gradient(ellipse at 90% 30%, #ede9fe 0, transparent 30%),
            #f8fafc;
    }
    .block-container {
        max-width: 1080px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }
    .hero-card {
        padding: 2.5rem 2.75rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 24px;
        background: linear-gradient(120deg, #102a43, #334e68 72%, #486581);
        box-shadow: 0 18px 45px rgba(16, 42, 67, 0.16);
        color: white;
    }
    .hero-eyebrow {
        margin: 0 0 0.75rem;
        color: #bfdbfe;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
    }
    .hero-card h1 {
        margin: 0;
        color: white;
        font-size: clamp(2.4rem, 6vw, 4rem);
        line-height: 1.08;
    }
    .hero-card p:last-child {
        margin: 0.9rem 0 0;
        color: #e2e8f0;
        font-size: 1.1rem;
    }
    [data-testid="stImage"] img {
        border: 5px solid white;
        border-radius: 22px;
        box-shadow: 0 12px 30px rgba(16, 42, 67, 0.16);
    }
    [data-testid="stForm"] {
        padding: 1.25rem;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        background: rgba(255, 255, 255, 0.8);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-card">
        <p class="hero-eyebrow">A little introduction</p>
        <h1>Hi, I'm Juhn Michael Bracho</h1>
        <p>Curious, learning, and building my first Streamlit app. 👋</p>
    </div>
    """,
    unsafe_allow_html=True,
)

image_column, profile_column = st.columns([0.85, 1.7], vertical_alignment="center")

with image_column:
    st.image("pitsur.jpeg", caption="Juhn Michael Bracho", use_container_width=True)

with profile_column:
    with st.container(border=True):
        st.subheader("A bit about me")
        st.write(
            "I'm Juhn Michael Bracho, and this is my first Streamlit web application. "
            "I'm glad you're here—feel free to say hello below!"
        )

st.markdown("### Leave a hello")
st.write("Add your name and I'll send a greeting your way.")

with st.form("visitor_greeting"):
    name = st.text_input("Your name", placeholder="Type your name here")
    submitted = st.form_submit_button("Send a hello 👋", type="primary")

if submitted:
    if name.strip():
        st.success(f"Nice to meet you, {name.strip()}! Thanks for stopping by.")
        st.balloons()
    else:
        st.warning("Add your name first, then send your hello.")

st.caption("Made with Streamlit · Juhn Michael Bracho")