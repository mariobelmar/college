Mes travaux de NLP
==================

Programme du 12 au 16 décembre
------------------------------

- **Lundi Matin**

   - Présentation du laboratoire

   - Rapide discussion avec les collègues/autres chercheurs et avec quelques
     autres stagiaires.

   - Présentation des locaux de mon maitre de stage.

- **Lundi après-midi** :

    - Discussion avec marc sur ce qu'on allait faire pendant le stage.

    - Manuel VALENTIN, ethnologue MNHN Responsable scientifique des collections
      d'ethnologie au Musée de l'Homme.

        - Visite des collections des objets du monde entier contemporain

- **Mardi matin**

   - Début du tri de document avec Taoues

- **Mardi après-midi**

   - Soutenance de thèse de Margaux BIEUVILLE, doctorante Université Paris Cité en
     Biodemographie, sur la biologie évolutive et le developpement.

   - Trier les documents

   - Début du code avec Marc(Maitre de stage)

- **Mercredi matin**

   - Trier les documents

   - Soutenance de thèse de Caroline GERARD, doctorante MNHN en primatologie sur la
     prise alimentaire des bonobos en RDC.

- **Mercredi après midi**

   - Avancement sur le code
   - Trier les documents(annexe 1)

- **Jeudi matin**

   - Avancement sur le code
   - Trier les documents

- **Jeudi après midi**

   - Marie-Claude Kergoat, Généticienne (Paléogénomique) CEA

   - Seminaire de recherche d'Aline THOMAS sur Momies et Insecte

   - Liliana HUET, gestionnaire MNHN des collections d'anthropologies et biologiques

       - Visite des collection anthropologique, cranes, squelettes, momies
         (collection jamais exposés) etc..

- **Vendredi matin**

   - Régis Regis DEBRUYNE, Anthropologue MNHN, paléogénéticien. Travaille sur la
     compréhension de l'évolution des éléphants il analyse donc les ancetres des
     éléphants(mamouth)

     - Travaille au Musée national d'histoire naturelle pour extraire informations
       génétiques des collections du musé

     - Activitée faite: Dillution d'adn d'un échantillon de vertèbre de poisson.(annexe
       2)

- **Vendredi après-midi**

  - Nicolas CESARD, ethno-entomologue MNHN

  - Paul VERDU, chercheur en génétique des populations CNRS, soutenance HDR sur
    "Histoires de Métissages"

Objectif
--------

- Avant le début du stage, avec mes parents et mon maitre de stage, nous nous étions mis
  d'accord pour qu'a la fin du stage j'ai appris a codé et a mettre en application la
  théorie du NLP , voici donc mes deux objectifs de programmations qui découlent de cette
  application:

  1. Mon premier objectif a été de produire un programme capable de donner les verbes et leur
     nombres de fois qu'ils apparaissent dans un texte.

  2. Mon deuxieme objectif a été de produire un programme capable de révéler la présence de typologies
     dans certaines langues a partir de mots clés.

     Ex: On a un livre sur l'abun (langue de nouvelle guinée) et je veux savoir si
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
librairies de nlp(annexe 4):

  - Méthodes basées sur des règles

  - Modèles de Machine Learning

  - Modèles de Deep Learning

Librairies et capacités
~~~~~~~~~~~~~~~~~~~~~~~

J'utilise la librairie nlp appelés Spacy, qui est assez récente mais plus rapide.
Voici ce dont est capable Spacy:

  1. La **tokenisation** ou **word segmentation**: découpé une phrase en plusieurs pièces, tokens.
      a. Ex: 'bonjour les amis' -> 'bonjour', 'les', 'amis'
  2. **lemmatization**: donner la forme canonique du mot, celle de base.
      b. Ex: 'trouvaient' -> 'trouver'
  3. **P.O.S tagging**: a partir de l'endroit ou se trouve le verbe
     dans la phrase on assigne au mot(token) sa nature.
      c. Ex: 'l'enfant mange une pomme' -> l'enfant : sujet | mange : verbe | etc..
  4. **dependency parsing**: dépendance a d'autre mots dans la phrase, c'est aussi le
     contexte, un mot peut changer le sens d'un autre mot.
      d. Ex: le mot 'que' peut signifier plein de chose

Grace a toutes ces étapes nous serons capable de produire un code qui, par exemple,
trouve le nombre de fois qu'apparait un mot dans un texte


Découverte du NLP
------------------

Je vais utiliser le langage appelé Python.  Un langage informatique est comme une langue
humaine, c'est une langue **compréhensible** par l'ordinateur. Il existe énormement de
langage different.

Premier code Python et Spacy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mots clés :

 - **fonction**: on donne a fonction une ou plusieurs choses et la fonction nous renvoit une
   version transformé de cette chose. Ex: on donne a la fonction deux chiffre et elle
   nous renvoit la somme des deux.


Exctraction de verbe
++++++++++++++++++++


On appelle la librairie spacy, c'est donc l'extension qui me permet de faire
plus de chose, ici de traiter des textes

.. code ::

  import spacy

Je cré une **fonction** a qui je donne le fichier qu'il va **tokeniser** donc rendre
lisible afin de l'analyser.

.. code ::

  def get_text_from_file:

Je cré une autre boucle qui trouve et ne renvoit que les verbes

.. code ::

    def get_only_verbs:

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

C'etait le premier code que j'ai pu faire. L'intétralité du code se trouve dans 'Mes
codes' a la fin du chapitre 3, conclusion.

Exctraction de typologies
++++++++++++++++++++++++++

Comme expliqué dans 'Objectifs' je vais 'extraire' certaines typologies de certaines
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

Elle récupère les mots 'tone' et 'tones'

.. code ::

    tones = [token for token in doc if token.text in ['tone', 'tones']]

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

Après cela il faut donc comparer cette médiane obtenue et le nombre d'occurrence des
mots-clés. Mais si ces deux données sont trop proche on arrive au degré d'incertitude,
il faut donc aussi prendre en compte cela.

La dernière étape consiste a mettre ces données dans un tableau(j'utilise la librairie
pandas pour faire les tableaux).

En Bref il faudra:

* Créer une fonction **mediane**

.. code ::

     def medianne(liste1):

Puis, il faut comparer la médianne avec les occurrences et produire un tableau avec
toutes les données.
Pour produire un tableau j'utilise une autre librairie appelé pandas.

         .. list-table:: tableau final d'extraction de typologies(ton et genre)
            :widths: 100 100 100 100 100 100
            :header-rows: 1
            :stub-columns: 0

            * - fichier analysé
              - typologie recherché
              - nb d'occurence
              - mediane du texte
              - difference
              - hasornot
            * - ani_2000_o
              - genders
              - 16
              - 1
              - 15
              - True
            * - aari_1994_o
              - genders
              - 6
              - 1
              - 5
              - True

- **difference** : comme dans l'ornigramme, k.occu - median_occurrence
- **hasornot**:existence de la typologie recherchée

.. mermaid::

  ---
  title : fonction qui compare la difference a la médiane
  ---

  flowchart TB
  nb("difference")
  ex("égale a mediane - nombre d'occurence")
  nb -.- ex
  N === i(incertitude)
  subgraph Ornigramme
    nb -->A{"> 1"}
    A -->|Yes| T("possède cette typologie")
    A -->|No| B{"< -1"}
    B -->|Yes| F("ne possède pas cette typologie")
    B -->|No| N("écart trop petit")
    end

