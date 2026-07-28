# JARVIS

JARVIS is a simple Python AI assistant based on the Iron Man assistant of the same name. JARVIS can be interacted with in either an IDE or in command prompt. JARVIS has knowledge on a variety of topics ranging from computer science, mathematics, engineering, general knowledge, and more. Commands that have been given to JARVIS are down below.

# How to Run JARVIS
## Disclaimer
- I apologize, but the model that needs to be downloaded in order to run this project takes up 9.1 GB of storage. I originally did not intend to publish this script, so I used a model that was larger and easier to train. For future projects, I will use models that are easier for others to download and run. I again apologize.

## Prerequisites
- **Git:** Required to clone the repository onto your computer. Can be downloaded from https://git-scm.com/install/windows.
- **Ollama:** Required to run the AI Model for this project. Can be downloaded from https://ollama.com/download/windows.
- **Python:** Required to run the project. I used Python 3 for this project.

## Instructions
1. **Navigate to your command prompt, then download the AI model `phi4:latest` from Ollama.**
```bash
ollama pull phi4:latest
```
2. **Install `ollama` and `psutil` to Python.**
```bash
pip install ollama psutil
```
3. **Clone the repository onto your computer.**
```bash
git clone https://github.com/rileynicholson/JARVIS.git
```
4. **`cd` to JARVIS.** 
```bash
cd JARVIS
```
5. **Run JARVIS either in an IDE or in command prompt.**
```bash
python main.py
```
&emsp; If the command does not work, try
```bash
python3 main.py
```

# Commands Built Into JARVIS
- `/read [File Path]` allows JARVIS to open and view files on your computer. This feature is valuable for programming advice, explaining a file, summarizing text, or teaching concepts highlighted in the text.
- `/monitor` has JARVIS display your computer's metrics. This is valuable for seeing how well your computer is running, or even to get JARVIS to explain what everything means!
- `exit`, `stop`, and `goodbye` are all commands that end your current conversation with JARVIS. Saying one of these 3 words solely in your prompt is how you get the program, and conversation, to stop.

# Future Updates to JARVIS
- I am not sure if I will add more features to JARVIS, but if I do, possible future features could include:
  - `/search [Input]` would allow JARVIS to search on the internet, similar to how users can have ChatGPT search the internet.
