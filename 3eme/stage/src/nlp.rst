Mes travaux de NLP
======================

Objectif
--------

- voir avec Marc

Théories
--------

Article de Marc:
    - :cite:p:`her2022defining`
    - :cite:p:`ulrich2021identifying`
    - :cite:p:`hammarstrom2020term`

Test de citation d'un article sur les nuages de mots :cite:p:`d2014recueils` pour le
voir dans la Bibliography de la fin du document.

Puis un test de citation en note de bas de page ici :footcite:p:`d2014recueils`

voir doc spacy pour plus d'info

  1. word segmentation
  2. lemmatization
  3. P.O.S tagging(trouver nature du mot)
  4. dependency parsing(dépendance a d'autre mots dans la phrase)

Découverte du NLP
------------------

Premier code Python et Spacy

Conclusion
==========


.. code ::

  import spacy
  import sys

  # Définir la langue (anglais)
  nlp = spacy.load("en_core_web_sm")
  NOVEL = '../../snt/ndm/alice.txt'

  def get_text_from_file(file: str) -> str:
      """
      ouvrir le fichier texte 'alice.txt' ou permettre a python de le lire 'r'
      myfile représente le fichier texte il peut donc en faire plusieurs chose
      """
      with open(file, 'r') as myfile:
          text = myfile.read()
      return text


  def get_only_verbs(ltext: str) -> list[str]:
      """
      for 'mot' in doc:
          if 'nature du mot' == verbe:
              verbe.append('infinitif du verbe')
      """
      doc = nlp(ltext)
      # verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
      verbs = []
      for token in doc:
          if token.pos_ == "VERB":
              verbs.append(token.lemma_)
      return verbs


  text = get_text_from_file(NOVEL)
  ltext = text[2000:4500]
  verbs = sorted(get_only_verbs(ltext))
  verbs_set = sorted(list(set(verbs)))
  # print(f'==> all words: {ltext}')
  print(f'==> only verbs there are {len(verbs)}: {verbs}')
  print('\n')
  print(f'==> only verbs without repetition there are {len(verbs_set)}: {verbs_set}')


Bibliography
=============

.. bibliography::

.. footbibliography::

