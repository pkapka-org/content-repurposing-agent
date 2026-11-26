import streamlit as st
from src.repurposer import repurpose

st.set_page_config(page_title="Content Repurposing Agent", layout="wide")
st.title("Content Repurposing Agent")
st.caption("Paste long-form content → get LinkedIn, Twitter, Email, Summary & Instagram instantly")

SAMPLE = """
Remote work has permanently changed how teams collaborate. Companies that embraced async communication
during the pandemic discovered something surprising: deep work improved. Without back-to-back meetings,
engineers shipped faster, writers produced better drafts, and designers iterated more freely.

But the shift came with trade-offs. Junior employees lost the informal mentorship that happens in offices.
Culture became harder to build. Spontaneous conversations — the kind that spark unexpected ideas — stopped
happening. Some companies responded with structured virtual coffee chats. Most failed.

The organizations that navigated this best did one thing differently: they were intentional about
synchronous time. They protected it for creative work, decision-making, and team bonding — and ruthlessly
eliminated it for status updates and information sharing that could be a document instead.

The future of work isn't remote or in-office. It's about knowing which mode serves which kind of work,
and building systems that make switching between them frictionless.
"""

col1, col2 = st.columns([4, 1])
with col1:
    if st.button("Load sample content"):
        st.session_state.content = SAMPLE.strip()
with col2:
    if st.button("Clear"):
        st.session_state.content = ""

content = st.text_area(
    "Paste your content here (blog post, article, transcript, notes…)",
    height=250,
    key="content"
)

if st.button("Repurpose Content", type="primary"):
    if not content.strip():
        st.warning("Please paste some content first.")
    else:
        with st.spinner("Repurposing with Qwen…"):
            try:
                result = repurpose(content)

                tab_summary, tab_linkedin, tab_twitter, tab_email, tab_instagram = st.tabs([
                    "Summary", "LinkedIn", "Twitter / X", "Email", "Instagram"
                ])

                with tab_summary:
                    st.subheader("Short Summary")
                    st.write(result.get("summary", ""))

                with tab_linkedin:
                    st.subheader("LinkedIn Post")
                    st.text_area("Copy this", result.get("linkedin_post", ""), height=250, key="li")

                with tab_twitter:
                    st.subheader("Twitter / X Thread")
                    thread = result.get("twitter_thread", [])
                    for tweet in thread:
                        st.info(tweet)

                with tab_email:
                    st.subheader("Email Newsletter Blurb")
                    st.text_area("Copy this", result.get("email_blurb", ""), height=180, key="em")

                with tab_instagram:
                    st.subheader("Instagram Caption")
                    st.text_area("Copy this", result.get("instagram_caption", ""), height=200, key="ig")

            except Exception as e:
                st.error(f"Error: {e}")
                st.info("Make sure Ollama is running (`ollama serve`) and the model is pulled (`ollama pull qwen2.5:1.5b`)")
