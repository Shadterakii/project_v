import requests


import os


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "vtuber_1"  # Default model

from openai import OpenAI


client = OpenAI(
    base_url="http://localhost:8880/v1", api_key="not-needed")


import pyaudio


def voice_output(inputstring):
    player = pyaudio.PyAudio().open(
        format=pyaudio.paInt16, 
        channels=1, 
        rate=24000, 
        output=True
    )
 
    with client.audio.speech.with_streaming_response.create(
        model="kokoro",
        voice="af_bella",
        response_format="pcm",
        input=inputstring
    ) as response:
        for chunk in response.iter_bytes(chunk_size=1024):
            player.write(chunk)


def send_message(messages):
    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    if response.status_code == 200:
        return response.json()["message"]["content"]
    else:
        print("❌ Error:", response.text)
        return None

def main():
    print("🤖 Ollama Chat (Model: {})".format(MODEL))
    print("Type `exit` to quit.\n")

    chat_history = []

    while True:
        user_input = input("🧍 You: ")
        if user_input.strip().lower() == "exit":
            break

        chat_history.append({"role": "user", "content": user_input})
        print("🤖 Akiyama Miku is thinking...")
        response = send_message(chat_history)

        if response:
            print("🤖 Akiyama Miku:", response)
            # voice_output(response)
            # print(type(response))
            chat_history.append({"role": "assistant", "content": response})
        else:
            print("❌ No response received.")

if __name__ == "__main__":
    main()