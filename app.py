import streamlit as st
from corrector import correct_text, get_suggestions

st.set_page_config(page_title="AI Spell Checker")

st.title("🧠 AI Spell & Grammar Corrector")

text = st.text_area("Enter text:")

if st.button("Correct"):
    if text:
        corrected = correct_text(text)

        st.subheader("Corrected Text:")
        st.write(corrected)

        st.subheader("Suggestions:")
        suggestions = get_suggestions(text)

        if suggestions:
            for s in suggestions:
                st.write(f"{s['error']} → {s['suggestions']}")
        else:
            st.write("No mistakes found")