# AI Social Media Caption Generator

A Streamlit web application that leverages the power of large language models (LLMs) through LangChain and the Groq API to generate creative and engaging social media captions.  Users can provide context, mood, and the target platform (e.g., Instagram, Twitter, LinkedIn) to receive tailored caption suggestions, complete with relevant hashtags.

## Features

* **Dynamic Prompt Engineering:** Captions are generated based on user-provided context, mood, and platform.
* **LLM-Powered Creativity:**  Uses a powerful LLM to produce unique and engaging content.
* **Platform-Specific Captions:** Optimizes captions for different social media platforms.
* **Hashtag Generation:** Suggests relevant and trending hashtags to increase visibility.
* **User-Friendly Interface:**  Built with Streamlit for a seamless user experience.
* **Model Statistics:** Displays information about the LLM's usage (tokens, completion time).
* **AI Thinking Process:** Shows the AI's internal "thoughts" during caption generation.
* **Copy to Clipboard:** Easily copy the generated caption with a single click.

## Technologies Used

* Python
* Streamlit
* LangChain
* langchain-groq
* Groq API


## Installation

1. Clone the repository:
   git clone https://github.com/aniket-1177/ai-social-media-caption-generator.git

2. Navigate to the project directory:
    cd ai-social-media-caption-generator

3. Create a virtual environment (recommended):
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Install the required packages:
    pip install -r requirements.txt

5. Set up your environment variables:
    Create a .env file in the project directory.
    Add your Groq API key: GROQ_API_KEY=your_actual_key

6. Usage
    Run the Streamlit app:
    streamlit run app.py
    Open the app in your browser at the provided URL.

