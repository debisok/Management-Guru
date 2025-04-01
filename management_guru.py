import streamlit as st
import random
from io import BytesIO
from fpdf import FPDF
import pandas as pd

# Expanded knowledge base with more insights
knowledge_base = [
    # (Same entries as before... truncated for brevity)
]

# Dashboard View
st.set_page_config(layout="wide")
st.title("📊 Management Guru Dashboard")

col1, col2 = st.columns([2, 3])

with col1:
    st.header("Ask the Experts")
    user_input = st.text_input("Your question")
    thinker_choice = st.radio("Choose your expert:", ("Peter Drucker", "Jack Welch", "Both", "Compare"))

with col2:
    st.header("Insight Display")

    def get_matching_insight(question, thinker):
        keywords = question.lower().split()
        candidates = [entry for entry in knowledge_base if thinker in ["Both", "Compare"] or entry["thinker"] == thinker]
        scored = []
        for entry in candidates:
            score = sum(1 for word in keywords if word in entry["topic"].lower() or word in entry["insight"].lower())
            scored.append((score, entry))
        scored.sort(reverse=True, key=lambda x: x[0])
        return scored

    insight_output = ""

    if st.button("Get Insight"):
        scored_entries = get_matching_insight(user_input, thinker_choice)

        if thinker_choice == "Compare":
            welch_entry = next((entry for score, entry in scored_entries if entry["thinker"] == "Jack Welch"), None)
            drucker_entry = next((entry for score, entry in scored_entries if entry["thinker"] == "Peter Drucker"), None)

            if drucker_entry:
                st.subheader("📘 Insight from Peter Drucker")
                st.write(drucker_entry["insight"])
                st.caption(f"Source: {drucker_entry['source']}")
                insight_output += f"Peter Drucker on {drucker_entry['topic']}\n{drucker_entry['insight']}\n\n"

            if welch_entry:
                st.subheader("📕 Insight from Jack Welch")
                st.write(welch_entry["insight"])
                st.caption(f"Source: {welch_entry['source']}")
                insight_output += f"Jack Welch on {welch_entry['topic']}\n{welch_entry['insight']}\n\n"

            if not welch_entry and not drucker_entry:
                st.warning("No insights matched your question. Try rephrasing.")

        else:
            top_entry = scored_entries[0][1] if scored_entries else random.choice(knowledge_base)
            st.subheader(f"💡 Insight from {top_entry['thinker']}")
            st.write(top_entry['insight'])
            st.caption(f"Source: {top_entry['source']}")
            insight_output += f"{top_entry['thinker']} on {top_entry['topic']}\n{top_entry['insight']}\n\n"

        # PDF download button
        if insight_output:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for line in insight_output.split('\n'):
                pdf.cell(200, 10, txt=line, ln=True)

            pdf_output = BytesIO()
            pdf.output(pdf_output)
            st.download_button(label="📄 Download Insight as PDF", data=pdf_output.getvalue(), file_name="insight.pdf", mime="application/pdf")

# Sidebar with Dashboard Table View
st.sidebar.title("📚 Browse All Insights")
if st.sidebar.checkbox("Show full knowledge base"):
    df = pd.DataFrame(knowledge_base)
    topic_filter = st.sidebar.multiselect("Filter by Topic", options=sorted(df["topic"].unique()))
    thinker_filter = st.sidebar.multiselect("Filter by Thinker", options=sorted(df["thinker"].unique()))
    keyword_search = st.sidebar.text_input("Search keywords in insight text")
    if topic_filter:
        df = df[df["topic"].isin(topic_filter)]
    if thinker_filter:
        df = df[df["thinker"].isin(thinker_filter)]
    if keyword_search:
        df = df[df["insight"].str.contains(keyword_search, case=False, na=False)]
    st.sidebar.dataframe(df[["thinker", "topic", "insight"]], height=500)

    # CSV export button
    csv_output = df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(label="⬇️ Download Filtered Insights as CSV", data=csv_output, file_name="filtered_insights.csv", mime="text/csv")

# Optional: Daily quote
if st.sidebar.button("Quote of the Day"):
    quote = random.choice(knowledge_base)
    st.sidebar.markdown(f"**{quote['thinker']} on {quote['topic']}**")
    st.sidebar.write(f"{quote['insight']}")
