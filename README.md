# Chatbot Project

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

## 📄 README.md
Essential information about the project, including setup instructions, usage guidelines, and contributors.

## 📄 LICENSE
License information for the project.

## Getting Started

1. Clone the repository: `git clone [repository_url]`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the chatbot: `streamlit run src/main.py`

Feel free to explore and adapt the structure to suit the specific needs of your chatbot project. If you have any questions, refer to the documentation or reach out to the project contributors.

Happy coding! 🤖✨
