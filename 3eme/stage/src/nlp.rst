Mes travaux de NLP
======================

PLAN
====

- Lundi après-midi :
  Marc
  Manel Valentin(ethnologue, responsable scientifique)
  visite des collections des objets du monde entier contemporain

- Mardi matin

  Trier les documents

    A. Bon de commande
    B. Ordre de mission

- Mardi après-midi

  - Soutenance de stage

  - Trier les documents:

    A. Bon de commande
    B. Ordre de mission

  - Code

- Mercredi matin
  - Trier les documents
  - Soutenance de stage

- Mercredi après midi
  - Trier les documents

- Jeudi matin
  - Trier les documents
  - Boxe

- Jeudi après midi
  - Marie Claude
  - Séminaire
  - Visite des collections d'ossements humains non présenté lors des expositions

- Vendredi matin

  - Régis: caractérisation d'ADN ancien 100% paléogénéticien travail sur la
    compréhension de l'évolution des éléphants il analyse donc les ancetres des
    éléphants(mamouth)

  - Etude:
    1. fac de biologie de l'évolution

    2. doctorat histoire de l'évolution de éléphants

  - travail au mnhn pour extraire informations génétiques des collections du musé

  - Travail fait:
    - dillution d'adn d'un échantillon de vertèbre de poisson
    - but -> que mangait les homme pré. le long de la Loire?

  1. Dillution de l'adn grace a une micro-pipette

     - déposer diluant
     - déposer adn dans le diluant

  2. Electrophorèse cappilaire

    Ajout de liquide fluoerescent pour la machine
    --> bande d'ADN

- Vendredi après-midi


Objectif
--------

- voir avec Marc

Théories
--------

Librairies et capacités
~~~~~~~~~~~~~~~~~~~~~~~

Article de Marc:
    - :cite:p:`her2022defining`
    - :cite:p:`ulrich2021identifying`
    - :cite:p:`hammarstrom2020term`

Test de citation d'un article sur les nuages de mots :cite:p:`d2014recueils` pour le
voir dans la Bibliography de la fin du document.

Puis un test de citation en note de bas de page ici :footcite:p:`d2014recueils`

Je utiliser la librairie nlp appelés Spacy, qui est assez récente mais plus rapide.
Voici le niveau d'analyse dont est capable Spacy:

  1. La tokenisation ou word segmentation: découpé une phrase en plusieurs pièces, token
     Ex: 'bonjour les amis' -> 'bonjour', 'les', 'amis'
  2. lemmatization: donner la forme canonique du mot celle de base.
     Ex: 'trouvaient' -> 'trouver'
  3. P.O.S tagging: a partir de l'endroit ou se trouve le verbe
     dans la phrase on assigne au mot(token) sa nature.
     Ex: 'l'enfant mange une pomme' -> l'enfant : sujet | mange : verbe | etc..
  4. dependency parsing: dépendance a d'autre mots dans la phrase, c'est aussi le
     contexte.
     Ex: un mot peut changer le sens d'un autre mot

Il en existe beaucoup d'autre manière d'analyser un texte mais elle seront beaucoup trop
longue a expliquées

Méthode d'apprentissage
~~~~~~~~~~~~~~~~~~~~~~~

Il existe pour l'instant 3 grandes familles d'aprentissage utilisés pour le nlp:

  - Méthodes basés sur des règles

      - résout des problèmes spécifiques (suprimer les spam a l'aide de mot clés 'promo')
      - rapidement inefficace face a la complexité du langage
  - Modèles de Machine Learning

      - compréhension du langage
      - utilise des données pré-traités
      - utilise d'autre procédés matématique et statistiques(longueur des phrases,
        occurrence de mots spécifiques)
  - Modèles de Deep Learning

      - Beaucoup plus complexes
      - intègre une énorme quantités de données pour essayer de créer un système proche
        de notre système neuronale


Découverte du NLP
------------------

Je vais commencer par vous expliquer le langage que je vais utiliser. C'est un langage
appelé Python.
C'est comme une langue humaine, c'est une langue **compréhensible** par l'ordinateur. Il
existe énormement de langage different.

Premier code Python et Spacy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mots clés :

 - **fonction**: on donne a fonction une ou plusieurs choses et la fonction nous renvoit une
   version transformé de cette chose. Ex: on donne a la fonction deux chiffre et elle
   nous renvoit la somme des deux.

On appelle la librairie spacy, c'est une sort d'extension qui me permet de faire
plus de chose, ici de traiter des textes
.. code ::

  import spacy

On définit la langue(ici anglais)
.. code ::

  nlp = spacy.load("en_core_web_sm")

Je cré une **fonction** a qui je donne le fichier qu'il va**tokenisé** donc rendre
lisible afin de l'analyser
.. code ::

  def get_text_from_file(file: str) -> str:

Je cré une autre boucle qui trouve et ne renvoit que les verbes 
.. code ::

    def get_only_verbs(ltext: str) -> list[str]:

Voila comment elle fonctionne:

- Elle commence par découper le texte (segmentation)...
.. code ::

      doc = nlp(ltext)

- Je cré une boucle qui prend chaque mot dans doc...
.. code ::

      if token.pos_ == "VERB":

- Si sa nature(token.pos) est un verbe...
.. code ::

        if token.pos_ == "VERB":

- Alors je l'ajoute a la liste vide appelé 'verbe'
.. code ::

            verbs.append(token.lemma_)


Version plus compact qu'on appelle une **liste compréhensive** (qui fait la meme chose)

.. code ::

      verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]



Conclusion
==========
.. code ::

  import spacy
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

.. bibliography::

.. footbibliography::

