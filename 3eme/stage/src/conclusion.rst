


Conclusion
==========


Mes codes
~~~~~~~~~

Premier code:

.. code ::

  import spacy
  nlp = spacy.load("en_core_web_sm")
  NOVEL = '../../snt/ndm/alice.txt'

  def get_text_from_file(file: str) -> str:
      with open(file, 'r') as myfile:
          text = myfile.read()
      return text


  def get_only_verbs(ltext: str) -> list[str]:
      doc = nlp(ltext)
      verbs = []
      for token in doc:
          if token.pos_ == "VERB":
              verbs.append(token.lemma_)
      return verbs

  text = get_text_from_file(NOVEL)
  verbs = sorted(get_only_verbs(ltext))
  verbs_set = sorted(list(set(verbs)))
  print(f'==> only verbs there are {len(verbs)}: {verbs}')
  print(f'==> only verbs without repetition there are {len(verbs_set)}: {verbs_set}')

Bibliography
=============

Article de Marc:
    - :cite:p:`her2022defining`
    - :cite:p:`ulrich2021identifying`
    - :cite:p:`hammarstrom2020term`

Test de citation d'un article sur les nuages de mots :cite:p:`d2014recueils` pour le
voir dans la Bibliography de la fin du document.
Puis un test de citation en note de bas de page ici :footcite:p:`d2014recueils`

.. bibliography::

.. footbibliography::

