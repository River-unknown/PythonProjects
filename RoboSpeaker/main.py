import os

if __name__ == '__main__':
    print("Welcome!!! I am RoboSpeaker 1.0.")
    while True:
        text = input("What do you want me to speak(press q if you are done): ")
        if text == "q":
            os.system(
                f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Bye Bye Friends\')"')
            break
        os.system(
         f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"')
