Armée, organisation
===================

Unité
------

Réorganistion majeur
~~~~~~~~~~~~~~~~~~~~

- par auguste:

  - salaire
  - retraite
  - crée un impot pour une caisse "aerium militare"
  - divisa en trois l'armée romaine :

    - garnison
    - marine
    - armées des frontières

- par septième Sévère:

  - effectif augmenté
  - salaire augmenté
  - sorte de congé payé
  - laissa de l'argent au soldat dans son testament

Garnison
---------

Prétoriens (garde impériale)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Le nombre des cohortes ainsi que des effectifs changent en fonctions des reformes des
empereurs. Mais en 27 les première cohortes prétoriennes sont crées : 9 cohortes
numérotés de 1 à 9

.. mermaid::

  flowchart TD

  subgraph cohortes prétorienne\n

    cohortes1(9 cohortes \n de 500 soldat \n + qqlq cavaliers)
    cohortes3(+ 3 cohorte x 500)
    cohortes4(+ 4 cohortes x1000 )
    cohortes9(moins 7 cohorte)
    cohortes7(9 cohortes x 500)
    cohortes1 --> cohortes3 --> cohortes4 --> cohortes9 -.-> cohortes7

  end


Toutes les cohortes étaient commandés par un chef de prétoires, 9 tribuns (1 par cohorte),
Chaque tribun controlait 6 centurion.

Après avoir pris part à la guerre civile et battu par Constantin 1er en 312 elles sont
dissoutes

Corhotes urbaines
~~~~~~~~~~~~~~~~~

Elles étaient au nombres de 3 numérotés de 9 à 12 (elles suivent les cohortes
prétoriennes) de 500 soldats (fantassins)

.. mermaid::

  flowchart TD

  subgraph cohortes urbaines \n
   urba1(3 cohortes de 500)
   urba2(+ 2 cohortes  *)
   urba3(3 premieres portées à 7)
   urba4(ramenées à 4 cohortes x 1000 )
   urba5(4 cohortes x 500)
   urba1 --> urba2 --> urba3 --> urba4 --> urba5

  end

\* Une d'entre elles furent installées à Lyon et l'autre à Carthage.

L'organistion des cohortes urbaines est la meme que celles des cohortes prétoriennes (c'est à dire : 1 prefet de prétoire, 6 tribuns, et 54 centurion).


.. mermaid::

  flowchart LR

  A(cohortes urbaine\n -- urbanici --)
  A --> B(police nocturne)
  A --> C(ronde pour prévenir les incendies)
  A --> D(gendarmerie municipale)
  A --> F(pompiers militarisés)
  G(pas d'armement,\n outils de pompiers)
  subgraph fonction
    B
    C
    D
  end
  subgraph nature
    F -.-> G
  end

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

  cohortes --> police & ronde & gendarmerie & pompier_m

Autre
~~~~~

En dehors des cohortes d'autres unités étaient crées par differents empereurs et  stationnés a Rome faisait aussi partit de la garnison.

- Auguste créa un corp spécial qui lui servait de garde du corp qui faisait environ 200 hommes.

- Idée qui fut reprise par Trajan qui forma les cavaliers gardes du corp, les equites singulares Augusti(1000)

- éclaireurs 300 (speculatores)

- primipilares qui étaient de vieux centurions servant de consillers au prince


Total
~~~~~

Les effectifs de la garnison ferait un peu moins de 15 000 soldats meme si ce chiffre, comme nous l'avons vu avec les cohortes prétoriennes, changeait souvent.


L'armée des frontières
======================

Principales forces
~~~~~~~~~~~~~~~~~~~

La principale force de l'armée romaine est la légion mais ce que les historiens oublient
souvent est le role joué  par les unités auxiliaires aussi nommé forces supplétives.

Légion
~~~~~~


