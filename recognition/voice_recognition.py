import os
import subprocess

import openai
from speech_recognition import Recognizer, AudioFile

from config import OPENAI_CONTENT


class AudioConverter:
    def __init__(self, file, language='ru-RU'):
        self.file = self.__convert_ogg_to_wav(file)
        self.language = language

    def convert(self):
        recognizer = Recognizer()
        with AudioFile(self.file) as audio_file:
            voice = recognizer.record(audio_file)
            recognizer.adjust_for_ambient_noise(audio_file)
        return recognizer.recognize_google(voice, language=self.language)

    def __convert_ogg_to_wav(self, file):
        file_path = file.replace('.ogg', '.wav')
        subprocess.run(['ffmpeg', '-v', 'quiet', '-i', file, file_path])
        # data, samplerate = soundfile.read(file)
        # soundfile.write(file.replace('ogg', 'wav'), data, samplerate)
        return file_path

    def openai_response(self, text):
        OPENAI_CONTENT[1]['content'] = text
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=OPENAI_CONTENT
        )
        return completion.choices[0].message.content

    def delete(self):
        os.remove(self.file.replace('wav', 'ogg'))
        os.remove(self.file)
