import spacy
import sys

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")


with open("alice.txt", 'r') as myfile:
    # Process whole documents
    text = myfile.read()
    mots = text.split()

text = text[2000:2400]


doc = nlp(text)


# Analyze syntax
# print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

verbes = [token.lemma_ for token in doc if token.pos_ == "VERB"]


# Find named entities, phrases and concepts
# for entity in doc.ents:
#     print(entity.text, entity.label_)

print(f'Dans Alice opdm il y a:\n'
      f' {len(mots)} mots\n'
      f'et dans un échantillon de 400 mots\n il y a {len(verbes)} verbe'
      f'en voici la liste:  {verbes}')

