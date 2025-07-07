# Chatbot Application

This project is a chatbot application built using Python, integrating the Gemini and Langchain libraries. It features a memory component to enhance user interactions and is designed to run locally using Streamlit.

## Project Structure

```
chatbot-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── chatbot.py       # Contains the Chatbot class
│   ├── memory.py        # Manages conversation memory
│   └── utils.py         # Utility functions
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore file
```

## Features

- **Chatbot Integration**: Utilizes Gemini and Langchain for generating intelligent responses.
- **Memory Management**: Remembers past interactions to provide contextually relevant responses.
- **Streamlit Interface**: A user-friendly web interface for interacting with the chatbot.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chatbot-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run src/main.py
   ```

## Usage Guidelines

- Open your web browser and navigate to `http://localhost:8501` to interact with the chatbot.
- Type your messages in the input box and press Enter to receive responses.
- The chatbot will remember previous interactions during the session.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.