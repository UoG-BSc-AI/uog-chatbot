# Chatbot Project

To run the project:

- Download Ollama: https://ollama.com/
- Run the command from terminal:
    -- ollama run stable-beluga
    -- Please know that you can always use another model. Ollama provides several choices. I am using 'stable-beluga'
    -- Stable-beluga is an LLM similar to ChatGPT but not as powerful. Since, it's small, we can run on the local system.
- 

--
TODO:

- Experiment with different models locally, and document the experiments results. I.e., ask model harmful, or irrelvant questions, or questions about various topics, and document the result within a CSV, by labelling whether the results are relevant/correct or not.
- Based on the experiment, you would recommend the best Open Source models. 

--
This repository contains the source code and resources for our chatbot project. The following explains the folder structure:

## 📂 src
- `main.py`: Entry point for the chatbot application.
- `modules/`: Directory for modular components or features.
    - `data_scrape.py`: Handles the data scraping of UoG website
    - `intents.py`: Handles intent recognition logic.
    - `responses.py`: Manages bot responses.

## 📂 data
- `training/`: Holds training data for the chatbot's natural language understanding.
    - `inputs.txt`: Training data
- `pretrained_models/`: Directory for storing pre-trained language models.

## 📂 models
- `saved_models/`: Location for storing trained chatbot models.

## 📂 docs
- `documentation.md`: Comprehensive documentation for the chatbot project.
- `api_reference.md`: Documentation for any APIs exposed by the chatbot.

## Getting Started

1. Clone the repository: `git clone [repository_url]`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the chatbot: `streamlit run src/🎓_University_of_Gloucestershire_Chatbot.py`

If you want to be part of the project, please reach out to the team or product manager
ushahid7@glos.ac.uk

Happy coding! 🤖✨
