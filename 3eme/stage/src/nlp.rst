Mes travaux de NLP
======================

Objectif
--------

Découverte du NLP
------------------



Théories
--------

Travaux pratiques
-----------------

Conclusion
==========

.. mermaid::

  flowchart LR
  a --> b
  a --> c
  
.. mermaid::

  flowchart LR

  cohortes(cohortes urbaine\n -- urbanici --)
  police(police nocturne)
  rondes(ronde pour prévenir les incendies)
  gendarmerie(gendarmerie municipale)
  pompier_m(pompiers militarisés)
  no_armes("pas d'armement,
            outils de pompiers")

  subgraph fonction
    police
    rondes
    gendarmerie
  end
  subgraph nature
    pompier_m -.-> no_armes
  end

  cohortes --> police & rondes & gendarmerie & pompier_m
  

