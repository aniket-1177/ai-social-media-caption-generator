import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os

from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

load_dotenv()  # Load environment variables from .env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ Groq API key not found. Please set the GROQ_API_KEY environment variable.")
    st.stop()

# Page Setup
st.set_page_config(page_title="Social Caption Generator", page_icon="📝", layout="centered")
st.title("🧠 AI Caption Generator")
st.caption("🚀 Generate catchy captions for social media")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Settings")
    selected_model = st.selectbox("Choose Model", ["deepseek-r1-distill-llama-70b"], index=0)
    st.markdown("### How It Works:")
    st.markdown("- 📝 Enter context, mood & platform")
    st.markdown("- 🔥 AI generates a perfect caption")
    st.markdown("- 📲 Copy & use instantly!")
    st.divider()
    st.markdown("Powered by [Groq API](https://groq.com/) | [LangChain](https://python.langchain.com/)")

# User Input Fields
st.subheader("📌 Enter Caption Details")
context = st.text_area("Describe the context (e.g., Vacation in Bali, Product launch, Birthday Party)", "")
# mood = st.selectbox("Choose a mood:", ["Fun", "Motivational", "Romantic", "Professional", "Inspirational"], index=0)
mood = st.text_input("Choose a mood (Fun, Motivational, Professional, Inspirational:", "")
platform = st.selectbox("Select platform:", ["Instagram", "Twitter", "LinkedIn", "Facebook", "Youtube",], index=0)
include_hashtags = st.checkbox("Include relevant hashtags?", value=True)

# Dynamic Prompt Engineering
def generate_prompt():
    prompt = f"""
    You are an expert in social media marketing. Generate an engaging, catchy caption based on:
    - **Context:** {context}
    - **Mood:** {mood}
    - **Platform:** {platform}
    - **Hashtags:** {'Yes' if include_hashtags else 'No'}
    
    **Guidelines:**
    - Make the caption resonate with {platform} users.
    - Keep it concise, engaging, and relevant.
    - Use appropriate emojis.
    """
    if include_hashtags:
        prompt += "\n- Suggest 3-5 trending hashtags relevant to the topic."
    
    return prompt

# Generate Caption
if st.button("✨ Generate Caption"):
    if not context.strip():
        st.warning("⚠️ Please enter some context before generating!")
    else:
        with st.spinner("🧠 AI is generating your caption..."):
            llm_engine = ChatGroq(model=selected_model, api_key=GROQ_API_KEY, temperature=0.5)
            ai_response = llm_engine.invoke(generate_prompt())

            # Extract clean response text
            response_text = ai_response.content if hasattr(ai_response, "content") else str(ai_response)

            # Separate "thinking" part and actual caption
            if "</think>" in response_text:
                thinking_part, final_caption = response_text.split("</think>")
                thinking_part = thinking_part.replace("<think>", "").strip()
                final_caption = final_caption.strip()
            else:
                thinking_part = "No additional thoughts generated."
                final_caption = response_text.strip()

            # Extract response metadata
            response_metadata = getattr(ai_response, "response_metadata", {})

        # Main Output Section (Left)
        col1, col2 = st.columns([2, 1])  # Left side (2/3) for caption, Right side (1/3) for extra info
        
        with col1:
            st.subheader("🔥 Your AI-Generated Caption:")
            st.write(final_caption)  # Display only the final caption
            
            # Copy button with session state
            if st.button("📋 Copy Caption"):
                st.session_state["copied_caption"] = final_caption
                st.success("✅ Caption copied to clipboard!")  # UI Feedback
        
        # Right Panel (Behind the Scenes + Model Stats)
        with col2:
            with st.expander("📜 **Behind the Scenes (AI Thinking Process)**", expanded=False):
                st.text_area("AI Thought Process:", value=thinking_part, height=150, disabled=True)

            with st.expander("📊 **Model Stats**", expanded=False):
                if response_metadata:
                    st.markdown(f"""
                    - **Model Used:** `{response_metadata.get('model_name', 'N/A')}`
                    - **Total Tokens:** `{response_metadata.get('token_usage', {}).get('total_tokens', 'N/A')}`
                    - **Completion Time:** `{response_metadata.get('token_usage', {}).get('completion_time', 'N/A')} sec`
                    - **Prompt Time:** `{response_metadata.get('token_usage', {}).get('prompt_time', 'N/A')} sec`
                    """)
                else:
                    st.warning("⚠️ No metadata available.")