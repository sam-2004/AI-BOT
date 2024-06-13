import datetime
import os
import fastapi
import openai
import speech_recognition as sr
import win32com.client
import webbrowser

openai.api_key = os.getenv("sk-proj-kdKNJWuUFkc3Hq2GC08wT3BlbkFJWGqphGbqfTVKCrffRd8j")
chatstr = ""
def chat(query):

    #write a program to use openai to generate a response
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        chatstr=f"SAM:{prompt}\n Jarvis",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    chatstr += f"{response['choices'][0]['text']}\n"
    return response['choices'][0]['text']

def ai(prompt):
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        text = f"OpenAI response for Prompt: {prompt} \n*************************\n\n{response['choices'][0]['text']}"
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
            with (open(f"Openai/{''.join(prompt.split('develop')[1:]).strip()}.txt", "w") as f):
                f.write(text)
    except Exception as e :
        speaker.Speak("An error occurred while generating the AI response.")

speaker = win32com.client.Dispatch("SAPI.SpVoice")

for voice in speaker.GetVoices() :
    if "Microsoft Zira Desktop" in voice.GetDescription():
        speaker.Voice = voice
        break

def takecommand ():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("listening")
        r.pause_threshold = 0.5
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said{query}")
            return query.lower()
        except Exception as e :
            return "some error occuerd sorry"

if __name__ == '__main__':
    print("listening for speech input")
   # command = takecommand()
    speaker.speak("hi im jarvis sir, how can i help you")
    print("Listening...")
    query = takecommand()
    # todo: Add more sites
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
             ["google", "https://www.google.com"], ]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            speaker.Speak(f"Opening {site[0]} sir...")
            webbrowser.open(site[1])
    # todo: Add a feature to play a specific song


    if "the time" in query:

        hour = datetime.datetime.now().strftime("%H")
        min = datetime.datetime.now().strftime("%M")
        speaker.Speak(f"Sir time is {hour} bajke {min} minutes")


    if "openai".lower() or "develop" in query.lower():
        ai(prompt=query)

    #else command.strip() :

     #   if "Play" in command or "search for song" in command:
      #      speaker.Speak("searching for the song on youtube")
       #     query = command.replace("play", "").replace("search for song", "").strip().replace(" ", "+")
        #    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    elif "develop" in query.lower():
        ai(prompt=query)

    elif " reset chat".lower() in query.lower():
        chatstr = ""

    elif "jarvis quit" in query:
        speaker.Speak("Goodbye, sir!")
        exit()


    else :
        chat(query)
