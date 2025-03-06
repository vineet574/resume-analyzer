
import streamlit as st
import spacy
import pdfplumber

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    return text

def analyze_resume(text):
    doc = nlp(text)
    s = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    return s

st.title("AI-Powered Resume Analyzer")

uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("Extracted Text")
    st.write(text[:500] + "..." if len(text) > 500 else text)

    skills = analyze_resume(text)
    st.subheader(" Skills")
    st.write(skills if skills else "No skills identified.")

