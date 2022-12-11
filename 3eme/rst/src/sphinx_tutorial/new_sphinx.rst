Install sphinx
===============

Request a new knowledge center to a manager
-------------------------------------------

.. important::

  Bellow the procedure to "manualy" create a new knowledge center based on sphinx from
  scratch.

  If you need a sphinx that will:

  - Automaticaly be on deployed on gitlab
  - Have a CI/CD that automaticaly deploy your knowledge center on
    https://knowledge.mazars.global
  - Provide an user management to control who can have access to you knowledge center

  Please request to a manager the creation of a documentation repository with `zf-make`

Manualy Setup a Sphinx
----------------------
The below documentation illustrate how to manualy setup a new Sphinx.

Pip Install and run ``sphinx-quickstart``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

  $ # create a requirements.txt with the following:
  cat requirements.txt
  furo
  sphinx==5.2.3
  sphinx-last-updated-by-git
  sphinx-view
  sphinx_inline_tabs
  sphinxcontrib.mermaid
  sphinx-copybutton
  $

  $ pip3 install -r requirement.txt
  ..
  $

.. code:: bash

  $ sphinx-quickstart  # answer questions with defaults options
  $ tree
  .
  ├── Makefile
  ├── README.rst
  ├── _build
  ├── _static
  ├── _templates
  ├── conf.py
  ├── index.rst
  ├── make.bat
  └── requirements.txt
  $

Create an ``src`` folder with some ``rst`` files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Create a nested "Table of contents", this will create fold/unfold left menu navigations.

.. mermaid::

   flowchart LR
     index(index.rst<br>conf.py) --> src/main.rst
     index --> src/sphinx_tutorial/index.rst
     src/sphinx_tutorial/index.rst --> sphinx_syntax_tutorial.rst
     src/sphinx_tutorial/index.rst --> mermaid_syntax_demo.rst
     src/sphinx_tutorial/index.rst --> new_sphinx.rst


.. tab:: Create ``.rst`` files on a ``src`` folder

  Create ``.rst`` files in ``src`` folder and point to them from root ``index.rst``

  .. code:: bash


    ├── conf.py
    ├── Makefile
    ├── requirements.txt
    ├── src
    │   ├── images
    │   │   └── logo_mazars.png
    │   ├── main.rst
    │   └── sphinx_tutorial
    │       ├── index.rst
    │       ├── sphinx_syntax_tutorial.rst
    │       ├── mermaid_syntax_demo.rst
    │       └── new_sphinx.rst
    └── index.rst                           <-- root index.rst

.. tab:: Root ``index.rst``

  ``index.rst`` point to ``/src/main.rst`` and to ``/src/sphinx_tutorial/index.rst``

  .. code:: bash

    $ cat index.rst

    Some title
    ===========

    .. toctree::
       :maxdepth: 2
       :caption: Contents:

       /src/main.rst
       /src/sphinx_tutorial/index.rst
    $


    $ cat src/sphinx_tutorial/index.rst

    Sphinx Tutorial
    ================

    .. toctree::
       :maxdepth: 3
       :caption: RST syntaxe to document serious projects:

       /src/sphinx_tutorial/sphinx_syntax_tutorial.rst
       /src/sphinx_tutorial/mermaid_syntax_demo.rst
       /src/sphinx_tutorial/new_sphinx.rst
    $

Configure Sphinx in ``conf.py``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure Sphinx in ``conf.py`` to have:

- furo style
- extentions (for autosectionlabel, tabs and Mermaid)
- pdf with LaTeX configuration

  - Install latex system on Linux with ``sudo apt-get install texlive-full``
  - To have mermaid on pdf add `mmdc <https://github.com/mermaid-js/mermaid-cli>`__

.. tab:: ``conf.py`` extentions

  On the ``conf.py`` update extentions list

  .. code:: python

    # in conf.py
    extensions = [
        'sphinx.ext.autosectionlabel',
        'sphinx_inline_tabs',
        'sphinx_last_updated_by_git',
        'sphinxcontrib.mermaid',
    ]
    autosectionlabel_prefix_document = True

.. tab:: furo style

  We use ``furo`` style

  .. code:: python

    # in conf.py
    html_theme = 'furo'

.. tab:: configure LaTeX

  To have beautiful pdf documentation from Sphinx update ``conf.py`` with the bellow:

  .. code:: python

    # in conf.py
    # -- Options for LaTeX output --------------------------------
    # title: warning latex syntax e.g. "my\_text" escape "_"
    # mermaid warning: to have mermaid on pdf add mmdc
    #   https://github.com/mermaid-js/mermaid-cli
    title = "put here your title\\newline\\large subtitle"
    latex_documents = [('index', 'my_documentation.tex', title, author, 'howto')]
    latex_elements = {
      'preamble': r'\usepackage{unicode-math}',
      'papersize': 'a4paper',  # 'letterpaper' or 'a4paper'
      'pointsize': '10pt',     # global fontsize, possible values are 10pt, 11pt and 12pt
      'sphinxsetup': 'hmargin={1.5cm,1.5cm}, vmargin={2cm,2cm}',
      # 'classoptions': ',twocolumn',    # to have two columns
      'tableofcontents': '',             # To remove the TOC
      }
    latex_theme = 'manual'  # two values: 'manual' to make a book, 'howto' to have an article
    latex_engine = 'xelatex'
    # latex_logo = 'src/images/logo_mazars.png'
    # https://sphinx-panels.readthedocs.io/en/latest/
    # sudo apt-get install texlive-extra-utils texlive-full

  You will be able to create pdf with:

  .. code:: bash

    $ make latexpdf
    ...
    $ evince _build/latex/my_documentation.pdf

