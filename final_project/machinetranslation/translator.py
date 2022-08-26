"""Code tells you how; Comments tell you why."""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

def language_translator(api_key, url):
    """Docstring"""
    authenticator = IAMAuthenticator(api_key)
    translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    translator.set_service_url(url)
    return translator

def english_to_french(english_text, api_key = API_KEY, url = URL):
    """Docstring"""
    #write the code here
    if english_text is None:
        return "No text."

    translator = language_translator(api_key, url)
    trans = translator.translate(
    english_text,
    model_id='en-fr').get_result()
    return trans["translations"][0]["translation"]


def french_to_english(french_text, api_key = API_KEY, url = URL):
    """Docstring"""
    #write the code here
    if french_text is None:
        return "No text."

    translator = language_translator(api_key, url)
    trans = translator.translate(
    french_text,
    model_id='fr-en').get_result()

    return trans["translations"][0]["translation"]

translation = english_to_french('Hello, how are you today?')
print(json.dumps(translation, indent=2, ensure_ascii=False))

translation = french_to_english("Bonjour, comment vous êtes aujourd'hui?")
print(json.dumps(translation, indent=2, ensure_ascii=False))
# l = translation["translations"][0]["translation"]
# print(l)
