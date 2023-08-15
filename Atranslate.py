from googletrans import Translator

'''
    For more info Documentations
 https://cloud.google.com/translate/docs/languages
 https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
 '''
def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

if __name__ == "__main__":
    text_to_translate = "Let's go!"
    target_language = "es" 

    translated_text = translate_text(text_to_translate, target_language)
    print(f"Original text: {text_to_translate}")
    print(f"Translated text: {translated_text}")

from translate import Translator

def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    translated_text = translator.translate(text)
    return translated_text

if __name__ == "__main__":
    text_to_translate = "Hello World Habibi!"
    target_language = "ar" 

    translated_text = translate_text(text_to_translate, target_language)
    print(f"Original text: {text_to_translate}")
    print(f"Translated text: {translated_text}")
