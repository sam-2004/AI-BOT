#Jarvis AI – A Python Voice Assistant

Jarvis is a voice-controlled AI assistant that listens to user commands, responds using OpenAI's GPT-3.5 model, opens websites, tells the time, and performs basic conversational tasks using speech synthesis and recognition.

Features

* Voice activation and recognition using `speech_recognition`.
* Text-to-speech using Microsoft's `SAPI.SpVoice`.
* Integration with OpenAI's GPT-3.5 for natural language processing.
* Open common websites like YouTube, Google, and Wikipedia.
* Tell the current time.
* Generate and save OpenAI responses.
* Extendable command system.


Installation

1. Clone the Repository

   ```bash
   git clone https://github.com/yourusername/jarvis-ai.git
   cd jarvis-ai
   ```

2. Create a Virtual Environment (Optional but recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install Requirements

   ```bash
   pip install -r requirements.txt
   ```

4.Set Environment Variable
   Set your OpenAI API key as an environment variable:

   ```bash
   export OPENAI_API_KEY="your-openai-api-key"  # For Linux/Mac
   set OPENAI_API_KEY=your-openai-api-key       # For Windows CMD
   $env:OPENAI_API_KEY="your-openai-api-key"    # For Windows PowerShell
   ```


Requirements

* Python 3.8+
* Packages:

  * `openai`
  * `speechrecognition`
  * `pywin32`
  * `fastapi` *(optional, currently unused)*
  * `pyaudio` *(needed for microphone input)*

Use this to install them manually:

```bash
pip install openai SpeechRecognition pywin32 pyaudio
```

---
 How It Works

* When run, Jarvis activates the microphone and listens for user commands.
* Based on keywords like "open YouTube" or "what's the time", it executes specific actions.
* For other inputs, it queries OpenAI's API and reads the response.
* It saves AI-generated responses related to "develop" prompts.

Notes

* Make sure your microphone is connected and permissions are granted.
* You must use **Microsoft Windows** to support `win32com.client` voice output.
* If you encounter errors with `pyaudio`, install it using wheels from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).

 To-Do

* Add functionality for playing music via YouTube.
* Use `fastapi` to build a GUI or web dashboard.
* Save chat history more efficiently.
* Add more dynamic site launching capabilities.
* Handle exceptions and errors gracefully.



MIT License

