import spacy
import sys

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

file = "alice.txt"

def get_text_from_file(file: str) -> str:
      with open(file, 'r') as myfile:
          text = myfile.read()
      return text


text = get_text_from_file(file)

doc = nlp(text)

verbes = [token.lemma_ for token in doc if token.pos_ == "VERB"]

print(f'Dans Alice opdm il y a:\n'
      f'et dans un échantillon de 400 mots\n il y a {len(verbes)} verbe'
      )
