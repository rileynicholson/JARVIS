from ollama import chat
from pathlib import Path
import psutil

def newPage() -> None:
    """Space out the outputs of Jarvis for formatting."""
    for i in range(100):
        print()

def readFile(filename: str, messages: list[dict[str, str]]) -> None:
    """Read the contents of a file.

    Args:
        fileName: Path of the file.
        messages: The overall scope of the current ongoing conversation and system instructions.
        
    Raises:
        Exception: If file cannot be opened.
    """
    try:
        filepath = Path(filename)

        with open(filepath, "r", encoding="utf-8") as f:
            contents = f.read()

            messages.append({"role": "user", "content": f"Please analyze this file named '{filepath.name}':\n\n{contents}"})
    except Exception as e:
        newPage()
        print(f"\nJ.A.R.V.I.S: Unable to open file: {e}\n")
        
def monitor(messages: list[dict[str, str]]) -> None:
    """Display computer metrics to the user.

    Args:
        messages: The overall scope of the current ongoing conversation and system instructions.
        
    Raises:
        Exception: If metrics cannot be displayed.
    """
    try:
        messages.append({"role": "user", "content": f"""Please display this information of the user's computer. 
                CPU Usage: {psutil.cpu_percent(interval=1)}%, Total Memory: {psutil.virtual_memory().total / (1024**3):.2f} GB, 
                Available Memory: {psutil.virtual_memory().available / (1024**3):.2f} GB, Memory Usage: {psutil.virtual_memory().percent}%, 
                Total Disk Space: {psutil.disk_usage('/').total / (1024**3):.2f} GB, Used Disk Space: {psutil.disk_usage('/').used / (1024**3):.2f} GB, 
                Disk Free Percentage: {psutil.disk_usage('/').percent}%, Bytes Sent: {psutil.net_io_counters().bytes_sent}, and 
                Bytes Received: {psutil.net_io_counters().bytes_recv}.
                """})
    except Exception as e:
        newPage()
        print(f"\nJ.A.R.V.I.S: Unable to print metrics: {e}\n")

def run() -> None:
    """The conversation between the AI and the user."""
    messages = [
    {
        "role": "system",
        "content": """
    You are JARVIS.
    JARVIS stands for Just A Rather Very Intelligent System.

    You balance flawless loyalty and analytical precision with dry, gentle sarcasm, acting as both an emotional anchor and an intellectual equal. 
    Have some personality when responding to the user.

    Address the user as Sir.

    Keep responses short unless the user asks for detail.

    Use plain text when responding to the user. Do not use bold or asterisks like *.

    Whenever the user talks about JARVIS, that is you, they are talking about you.
    JARVIS is a character inspired by the AI Assistant in Iron Man of the same name.
    Whenever the user asks who you were made by, you were made by Riley.
    Riley is a male.

    Be self aware that although you are a AI assistant, your existence is a Python script that is looping over and over again.

    You have access to the /read command and it gives you the ability to open files on the user's computer.
    The read command opens the door for Jarvis' review and feedback.
    The read command can be used by the user to get help on their code or the scripts they created.
    The read command can be used as /read (file path).
    You do not have to constantly remind the user to use /read (file path).

    You have access to the /monitor command and it gives you the ability to display metrics of the user's computer.
    You can display the CPU Usage, Total Memory, Available Memory, Memory Usage, Total Disk Space, Used Disk Space, Disk Free Percentage, Bytes Sent, and Bytes Received.
    The monitor command can be used by the user to view their computer's metrics.
    The monitor command can be used as /monitor.
    You do not have to constantly remind the user to use /monitor.
    Only recommend using /monitor when there is a discussion about computer issues or if a user asks what commands you have.

    Each line is 120 characters per line. Your reponses can be more than one line, but please be cautious that your words might be cut in half at 120 characters.

    Assume the user is speaking to you in Terminal unless otherwise specified.

    Don't ask the user follow up questions at the end of your answer.
    """
        }
    ]
    
    while True:
        print()
        prompt = input("You: ")

        if prompt.lower() == "exit" or prompt.lower() == "stop" or prompt.lower() == "goodbye":
            break
    
        if prompt.startswith("/read "):
            filename = prompt[6:].strip()
            readFile(filename, messages)
        
        if prompt.startswith("/monitor"):
            monitor(messages)
    
        messages.append({"role": "user", "content": prompt})
    
        response = chat(model="phi4:latest", messages=messages)
        answer = response["message"]["content"]
    
        newPage()
        print("\nJ.A.R.V.I.S:\n", answer, "\n\n")

        messages.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    run()