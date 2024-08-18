from googletrans import Translator, LANGUAGES

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translation = translator.translate(text, src=src_lang, dest=dest_lang)
    return translation.text

def main():
    print("Welcome to the Multilingual Translator App")
    print("Supported languages:")
    for lang_code in LANGUAGES:
        print(f"{lang_code}: {LANGUAGES[lang_code]}")

    src_lang = input("Enter the source language code: ")
    dest_lang = input("Enter the destination language code: ")
    text = input("Enter the text to translate: ")

    translated_text = translate_text(text, src_lang, dest_lang)
    print(f"Translated text: {translated_text}")

if __name__ == "__main__":
    main()
