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

