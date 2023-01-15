Conclusion
==========

Appréciation personnelle
------------------------

- Ce stage a été pour moi une belle expérience, très enrichissante qui m'a permis de
  découvrir l'essentiel du métier. Entouré de toute l'équipe qui m'ont chacun montré
  leur rôle dans l'entreprise, j'ai pu observer les méthodes de travail et constater les
  réalités du métier.

- Au delà du fait que ce stage a été pour moi une merveileuse découverte de la vie active,
  il ne m'a pas permis de confirmer mon choix quand à mes futurs interets professionnels qui
  seront surement tournés vers la médecine. Le monde l'informatique, et pas de la
  recherche, quant a lui m'interese énormement.

- J'ai aussi pu atteindre mes deux objectifs de programmations, qui sont tous les deux
  détaillés dans ce rapport.

- Après avoir longuement parlé avec mon maitre de stage, j'ai pu trouvé de nombreux points
  positifs et quelques points négatifs:

  - **points positifs**

     - Liberté de travail
     - Liberté d'horaires
     - Atmoshpère général du laboratoire
     - fonctionnaire donc si le laboratoire ferme, ils ont la garantie de
       trouver du travail dans une autre société

  - **points négatifs**

     - salaire peu élevé
     - infrastructure interne (internet, cable) baclée

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


Annexe
======

Annexe 1. 
----------

Recherche, enseignement, collections, diffusion, valorisation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    - Recherche: Découvrir, apprendre pour ensuite faire de la diffusion et de la
      valorisation.
    - Enseignement: Donner des cours dans les universités, c'est essentiellement le
      travail des enseignants chercheurs
    - Collections: Restaurer, entrenir, repertorier les collections du muséum
    - Diffusion: Rendre le travail des chercheurs "publiques", l'expliquer a la télé
      pour informer des découvertes, par exemple.
    - Valorisation: Plus sérieux que la Diffusion, c'est publier ses recherches dans
      une revue scientifique.


Annexe 2.
---------

Trie des documents avec Taoues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Taoues s'occupe de toute l'administration du laboratoire EA UMR 7206,
  elle est la Responsable administrative et la secrétaire générale.

- Elle nous, moi et d'autres stagiaires, a donc donner pour taches de trier les
  documents du laboratoire.

- Nous devions séparer ces documents d'abord par établissement (CNRS et MNHN),
  puis encore les séparer en bon de commande et  ordre de mission.

  - Bon de commande: le muséum(MNHN) ou le CNRS a besoin d'un nouvel objet, il doit donc
    expliquer a la direction pourquoi il en a besoin et combien il en veut.

  - Ordre de mission: Lorsqu'un chercheur, enseignant-chercheur ou support doit partir
    quelque part il doit laisser une trace et dire a la direction ou il part cela
    justifie qu'il ne soit pas au 'bureau'.

- Cette tache nous a pris plus de 10h tout le long de la semaine de stage.

Annexe 3.
---------

Dillution d'adn d'un échantillon de vertèbre de poisson.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 but: que mangait les hommes préhistoriques le long de la Loire?

   1. dillution d'adn d'un échantillon de vertèbre de poisson a l'aide d'un
     micro-pippette

     A. déposer diluant
     B. déposer adn dans le diluant

   2. Electrophorèse cappilaire

     A. Ajout de liquide fluoerescent pour la machine
     B. resultat: bande d'ADN

Annexe 4.
---------

Méthode d'apprentissage de NLP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  - Méthodes basées sur des règles

      - résout des problèmes spécifiques (suprimer les spam des boites mail a l'aide de
        mot clés 'promo')
      - rapidement inefficace face a la complexité du langage humain.
  - Modèles de Machine Learning

      - compréhension avancée du langage
      - utilise des données pré-traités
      - utilise d'autre procédés matématique et statistiques(longueur des phrases,
        occurrence de mots spécifiques)
  - Modèles de Deep Learning

      - Beaucoup plus complexes
      - intègre une énorme quantités de données pour essayer de créer un système proche
        de notre système neuronale
