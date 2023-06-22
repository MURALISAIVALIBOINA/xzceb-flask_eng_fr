""" These lines of code are used for translation . """

from deep_translator import GoogleTranslator ,MyMemoryTranslator

def english_to_french(english_text):
    """
    This is an English to French translator.
    """
    french_text = GoogleTranslator(source='en', target='fr').translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """
    This is a French to English translator.
    """
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    print(english_text)
    return english_text
