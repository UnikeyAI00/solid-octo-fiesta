import streamlit as st
import json
from crew import run_crew

st.title("RBI Regulatory Compliance Dashboard")

if st.button("Start Compliance Check"):
    st.write("🔄 Running CrewAI agents... Please wait.")
    result = run_crew()
    
    st.subheader("📑 Compliance Report:")
    st.text_area("Generated Report:", value=result, height=300)

    # Save Report as JSON
    with open("compliance_report.json", "w") as f:
        json.dump(result, f)

    st.download_button("📥 Download Report", "compliance_report.json", "application/json")

st.write("✅ Click 'Start Compliance Check' to begin processing RBI regulations.")
