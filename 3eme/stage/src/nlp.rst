Mes travaux de NLP
======================

Programme
----------

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

- Mon premier objectif a été de produire un programme capable de donner les verbes et leur
  nombres dans un texte

- Mon deuxieme a été de produire un programme capable de révéler la présence de typologies
  dans certaines langues a partir de mots clés.
  Je cherche dans une 'grammaire'(petit livre contenant l'intégralité de la grammaire d'une
  langue)sous forme numérique la présence de typologie par mots clés.

  Ex: On a une grammaire sur l'abun (langue de nouvelle guinée) et je veux savoir si
  cette langue contient un système de ton, je vais donc chercher le nombre de fois
  qu'apparait le mot 'ton', et en fonction de cela je vais décider si la langue contient
  oui ou non un système de ton.

Théories
--------

Le nlp est une branche de la programmation qui s'est développée il y a une dizaine
d'années. Son but est que les ordinateurs puissent comprendre les langues humaines mais
surtout qu'ils puissent les analysées et de traité des textes

Méthode d'apprentissage
~~~~~~~~~~~~~~~~~~~~~~~

Il existe pour l'instant 3 grandes familles d'aprentissages utilisées pour les
librairies de nlp:

  - Méthodes basées sur des règles

      - résout des problèmes spécifiques (suprimer les spam des boites mail a l'aide de
        mot clés 'promo')
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

Librairies et capacités
~~~~~~~~~~~~~~~~~~~~~~~

J'utilise la librairie nlp appelés Spacy, qui est assez récente mais plus rapide.
Voici ce dont est capable Spacy:

  1. La tokenisation ou word segmentation: découpé une phrase en plusieurs pièces, token
     Ex: 'bonjour les amis' -> 'bonjour', 'les', 'amis'
  2. lemmatization: donner la forme canonique du mot, celle de base.
     Ex: 'trouvaient' -> 'trouver'
  3. P.O.S tagging: a partir de l'endroit ou se trouve le verbe
     dans la phrase on assigne au mot(token) sa nature.
     Ex: 'l'enfant mange une pomme' -> l'enfant : sujet | mange : verbe | etc..
  4. dependency parsing: dépendance a d'autre mots dans la phrase, c'est aussi le
     contexte.
     Ex: un mot peut changer le sens d'un autre mot

Grace a toutes ces étapes nous serons capable de produire un code qui, par exemple,
trouve le nombre de fois qu'apparait un mot dans un texte


Découverte du NLP
------------------

Je vais commencer par vous expliquer le langage que je vais utiliser. C'est un langage
appelé Python.
Un langage informatique est comme une langue humaine, c'est une langue
**compréhensible** par l'ordinateur. Il existe énormement de langage different.

Premier code Python et Spacy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mots clés :

 - **fonction**: on donne a fonction une ou plusieurs choses et la fonction nous renvoit une
   version transformé de cette chose. Ex: on donne a la fonction deux chiffre et elle
   nous renvoit la somme des deux.


Premier code
+++++++++++++


On appelle la librairie spacy, c'est une sorte d'extension qui me permet de faire
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

.. code ::

            verbs.append(token.lemma_)

Version plus compact qu'on appelle une **liste compréhensive** (qui fait la meme chose)

.. code ::

      verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]

C'etait le premier code que j'ai pu faire. L'intétralité du code se trouve dans 'Mes
codes'

Deuxième code
+++++++++++++

Comme expliqué dans 'Objectifs' je vais rechercher certaines typologies de certaines
langues. Je vais donc me concentrer sur la présence de Tons(en chinois mais aussi en
espagnol), et la présence de genre(masc / fem / neut / etc...).
Pour cela je vais choisir des mots clés, ici ce sera très facile, qui seront 'tone' et
'gender' (mes pdf sont en anglais), dans certains cas il est plus compliqué de trouvé
les bons mots clés(pour les système de multplication)

J'ai donc une première fonction qui me permet de me donner le nombre de fois qu'apparait les mot
'tone' et 'tones'. Cette fonction est assez similaire au programme qui me renvoit les
verbes.

.. code ::

  def test_all_files(text):

Elle récupère les mots 'gender' et 'genders'

.. code ::

    genders = [token for token in doc if token.text in ['gender', 'genders']]

Elle récupère les mots 'tone' et 'tones'

.. code ::

    tones = [token for token in doc if token.text in ['tone', 'tones']]

Si on schématise cette fonction cela donnerait

.. mermaid ::

  flowchart LR
  a[(test_all_files)]
  file(fichier texte / grammaire)
  return(toutes les fois qu'apparait les mots tone et gender)
  classDef red fill:#ff4040
  file ==> a:::red ==> return

A partir de la je vais vous expliquer d'abord le fonctionnement de la suite du
programme.
Après avoir récupéré le nombre d'occurences de mes mots clés, je vais pouvoir savoir si
la langue possède bien ces typologies. Pour cela il faudra que je compare ce nombre
d'occurences par rapport au reste du texte. Il y a plusieurs méthode.

    - Calculer la moyenne
        Problèmes: les mots appelés fonctions (the, of, etc..) vont réhausser la moyenne.
        C'est le principe

    - **Calculer la médiane**
        C'est la méthode que je vais utiliser

    - Autre méthode de marc

Après cela il faut donc comparer cette médiane obtenue et le nombre d'occurrence des
mots-clés. Mais si ces deux données sont trop proche on arrive au degré d'incertitude,
il faut donc aussi prendre en compte cela.

La dernière étape consiste a mettre ces données dans un tableau(j'utilise la librairie
pandas pour faire les tableaux).

En Bref il faudra:

      1. créer une fonction **mediane**

         .. def medianne(liste1):

      2. comparer la médianne avec les occurrences

         .. mermaid::

           flowchart TB

           nb("difference")
           ex("égale a mediane - nombre d'occurence")
           nb -.- ex
           t -.-  T("possède cette typologie")
           f -.- F("ne possède pas cette typologie")
           n -.- N("écart trop petit")
           N === i(incertitude)
           subgraph Ornigramme
             nb -->A{"> 1"}
             A -->|Yes| t(True)
             A -->|No| B{"< -1"}
             B -->|Yes| f(False)
             B -->|No| n(None)
             end

      3. produire un tableau avec toutes les données


.. list-table::
   :widths: 50 50 50 50 50 50
   :header-rows: 1
   :stub-columns: 0

   * - Langue/grammaires
     - gender/tone
     - k.occu
     - median_occurence
     - difference
     - hasornot
   * - ani_2000_o
     - genders
     - 16
     - 1
     - 15
     - True
   * - ani_2000_o
     - tones
     - 7
     - 1
     - 6
     - True
   * - aari_1994_o
     - genders
     - 6
     - 1
     - 5
     - True
   * - aari_1994_o
     - tones
     - 0
     - 1
     - -1
     - None

- **Fichier/grammaires** : fichier analysé
- **gender/tone** : typologie recherché
- **k.occu** : nombre de fois qu'apparait le mots clé
- **median_occurrence** : mediane du texte
- **difference** : comme dans l'ornigramme, k.occu - median_occurrence
- **hasornot** : existence de la typologie recherchée


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


Conclusion
==========


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

