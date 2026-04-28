import streamlit as st
from corrector import correct_text, get_suggestions, grammar_score

st.set_page_config(
    page_title="AI Spell & Grammar Corrector",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.stApp{
    background: linear-gradient(-45deg, #0f172a, #1e1b4b, #0f766e, #4c1d95);
    background-size: 400% 400%;
    animation: aurora 12s ease infinite;
    color: white;
}

@keyframes aurora{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}

.main-box{
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(20px);
    box-shadow: 0 0 30px rgba(255,255,255,0.1);
}

h1,h2,h3,p,label{
    color:white !important;
}

.stTextArea textarea{
    background: rgba(255,255,255,0.12) !important;
    color: white !important;
    border-radius: 15px !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
}

.stButton button{
    width:100%;
    border-radius:15px;
    height:55px;
    font-size:18px;
    font-weight:bold;
    background: linear-gradient(90deg,#00f5d4,#00bbf9);
    color:black;
    border:none;
}

.stButton button:hover{
    transform: scale(1.02);
    transition: 0.3s;
}

.result-box{
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 15px;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 AI Spell & Grammar Corrector")
st.write("Fix spelling mistakes, improve grammar, and write smarter.")

st.markdown('<div class="main-box">', unsafe_allow_html=True)

text = st.text_area(
    "Enter your text:",
    height=220,
    placeholder="Example: I am gud in englih and i luv msging u..."
)

if st.button("✨ Correct Text"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Checking your text..."):
            corrected = correct_text(text)
            suggestions = get_suggestions(text)
            score = grammar_score(text)

        st.subheader("✅ Corrected Text")
        st.markdown(
            f'<div class="result-box">{corrected}</div>',
            unsafe_allow_html=True
        )

        st.subheader("📊 Grammar Score")
        st.progress(score)
        st.write(f"Score: {score}%")

        st.subheader("🛠 Suggestions")
        if suggestions:
            for s in suggestions:
                st.write(f"• **{s['error']}** → {s['suggestions']}")
        else:
            st.write("No mistakes found 🎉")

st.markdown('</div>', unsafe_allow_html=True)