from googletrans import Translator

translator = Translator(service_urls=['translate.google.com'])
text_to_translate = "Hello, how are you?"

# translate() method is used to translate the text
translated_text = translator.translate(text_to_translate, dest='hi').text

print(translated_text)
