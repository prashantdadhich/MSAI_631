# Simple Traditional Chatbot Project

This project is a simple **traditional (non-LLM, rule-based) chatbot** written in Python.  
It was prepared to meet a coursework requirement for building a chatbot that:

- responds to multiple prompts
- lists its capabilities
- handles malformed or unknown input gracefully
- can be extended later

## Project Files

- `simple_chatbot.py` - main chatbot application
- `requirements.txt` - project dependencies
- `.gitignore` - recommended Git ignore file
- `sample_output.txt` - example interaction
- `README.md` - project overview and run instructions

## Requirements

- Python 3.8 or later

No external libraries are required for this version.

## How to Run

1. Open a terminal in this project folder
2. Run:

```bash
python simple_chatbot.py
```

## Example Questions You Can Ask

- `hello`
- `what is your name`
- `what can you do`
- `how are you`
- `who made you`
- `date`
- `time`
- `help`
- `exit`

## Chatbot Design

This chatbot uses a **rules-based approach**:
1. The program accepts user input
2. The input is normalized using `strip()` and `lower()`
3. The program checks the text against a set of predefined rules
4. A matching response is returned
5. If no rule matches, the chatbot provides a fallback response

## Suggested GitHub Repository Structure

```text
simple-traditional-chatbot/
├── .gitignore
├── README.md
├── requirements.txt
├── sample_output.txt
└── simple_chatbot.py
```

## GitHub Upload Steps

1. Create a new GitHub repository
2. Upload all files in this folder
3. Commit with a message such as:
   - `Initial commit for simple traditional chatbot project`
4. Copy the repository URL and include it in your report

## Possible Future Enhancements

- Add more intents and responses
- Add current date/time using Python libraries
- Add a GUI with Tkinter
- Add logging
- Convert it into a web app with Flask
- Extend it toward NLP or machine learning

## License

This project is for educational use.
