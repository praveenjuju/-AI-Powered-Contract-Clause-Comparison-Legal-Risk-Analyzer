import streamlit as st
from app.analyzer import analyze_contract
from app.nlp_utils import extract_clauses_from_docx, extract_clauses_from_pdf

st.title("AI-Powered Legal Risk Analyzer")
uploaded_file = st.file_uploader("Upload contract (.pdf or .docx)", type=["pdf", "docx"])

if uploaded_file:
    if uploaded_file.name.endswith(".pdf"):
        clauses = extract_clauses_from_pdf(uploaded_file)
    else:
        clauses = extract_clauses_from_docx(uploaded_file)
    
    results = analyze_contract(clauses)
    
    st.subheader("Analysis Results")
    for clause, result in results:
        st.markdown(f"**Clause:** {clause}")
        st.markdown(f"🔍 **Risk Level:** `{result}`")
        st.markdown("---")
