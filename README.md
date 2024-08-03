# Langchain-Prompts-Demo-with-Azure-OpenAI
This repository contains a demo application showcasing the integration of Azure OpenAI with LangChain to perform various natural language processing tasks using Streamlit. This demo illustrates the power and versatility of Azure OpenAI's language models when combined with LangChain for prompt engineering.

## Features

- **Sentiment Analysis**: Determines the sentiment of a given product review.
- **Emotion Identification**: Identifies a list of emotions expressed in a review.
- **Language Translation**: Translates text from any language to English.
- **Tone Conversion**: Converts slang text into a formal business letter.
- **AI Assistant for Emails**: Generates professional email responses based on customer reviews and sentiments.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Langchain-Prompts-Demo-with-Azure-OpenAI.git
    cd Langchain-Prompts-Demo-with-Azure-OpenAI
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your environment variables. Create a `.env` file in the root directory and add the following:
    ```
    OPENAI_API_TYPE=your_openai_api_type
    OPENAI_API_KEY=your_openai_api_key
    OPENAI_API_BASE=your_openai_api_base
    OPENAI_API_VERSION=your_openai_api_version
    DEPLOYMENT_NAME=your_deployment_name
    OPENAI_MODEL_NAME=your_openai_model_name
    ```

## Usage

Run the Streamlit app:
```sh
streamlit run app.py


**## About Me**
I am a passionate software developer with experience in building applications using AI and machine learning technologies. This demo project is part of my efforts to explore the capabilities of Azure OpenAI and LangChain for advanced NLP tasks. Feel free to reach out to me on LinkedIn or Twitter.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.**
