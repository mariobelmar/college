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

Annexe 1. Recherche, enseignement, collections, diffusion, valorisation
-----------------------------------------------------------------------

    - Recherche:
    - Enseignement: Donner des cours dans les universités, c'est essentiellement le
      travail des enseignants chercheurs
    - Collections: Restaurer, entrenir, repertorier les collections du muséum
    - Diffusion: Rendre le travail des chercheurs "publiques", l'expliquer, par exemple,
      a la télé pour informer des découvertes, par exemple.
    - Valorisation: Plus sérieux que la Diffusion, c'est publier ses recherches dans
      une revue scientifique.


Annexe 2. Trie des documents avec Taoues
----------------------------------------

Taoues s'occupe de ... elle est la ...
J'ai du séparer ... des ...
Avec ...(personnes)...

Annexe 3. Dillution d'adn d'un échantillon de vertèbre de poisson.
------------------------------------------------------------------

 but: que mangait les homme pré. le long de la Loire?

   1. dillution d'adn d'un échantillon de vertèbre de poisson a l'aide d'un
     micro-pippette

     A. déposer diluant
     B. déposer adn dans le diluant

   2. Electrophorèse cappilaire

     A. Ajout de liquide fluoerescent pour la machine
     B. resultat: bande d'ADN
