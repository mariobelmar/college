Sphinx Syntax Tutorial
=========================
We use *restructuredtext* aka **rst** syntax to document our project with Sphinx

- `rst online ressources
  <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_

Paragraphs and notes
------------------------
.. tab:: Paragraphs and Notes

  This is a paragraph.

  Paragraphs line up at their left edges, and are normally separated by blank
  lines.

  .. note::

     You can decorate a block as a **note**

  .. warning::

     Or as a **warning**, please try *attention*, *caution*, *danger*,
     *error*, *hint*, *important* and *tip* too.

.. tab:: Paragraphs and Notes -- code

  .. code::

    This is a paragraph.

    Paragraphs line up at their left edges, and are normally separated by blank
    lines.

    .. note::

       You can decorate a block as a **note**

    .. warning::

       Or as a **warning**, please try *attention*, *caution*, *danger*,
       *error*, *hint*, *important* and *tip* too.


tabs images and code
--------------------
.. tab:: Tab with an image

   .. image:: /src/images/logo_mazars.png
      :width: 400px

.. tab:: Tab with some code

   .. code:: python

     def fibs():
        """
        This code does not work ;)
        """
        a = 0
        b = 1
        while True:
            yield a
            a, b = b, a + b

.. tab:: How to create this tabs ?

   .. code::

      .. tab:: Tab with an image

         .. image:: /src/images/logo_mazars.png
            :width: 400px

      .. tab:: Tab with some code

         .. code:: python

           def fibs():
              """
              This code does not work ;)
              """
              a = 0
              b = 1
              while True:

Tables
--------
.. list-table::
   :widths: 30 10 60
   :header-rows: 1
   :stub-columns: 0

   * - Queue
     - Nb
     - Details
   * - big_jobs_few_tasks
     - 2
     - Non igitur potestis voluptate omnia dirigentes
   * - small_jobs_many_tasks
     - 10
     -
   * - lazy_table_injection
     - 4
     - Videamus animi partes, quarum est conspectus illustrior;

.. tab:: Generic Table (**list-table** the best/simpler syntax)

   .. code::

     .. list-table::
        :widths: 30 20 50
        :header-rows: 1
        :stub-columns: 0

        * - Queue
          - Nb
          - Details
        * - big_jobs_few_tasks
          - 2
          - Non igitur potestis voluptate omnia dirigentes
        * - small_jobs_many_tasks
          - 10
          -
        * - lazy_table_injection
          - 4
          - Videamus animi partes, quarum est conspectus illustrior;

.. tab:: Table (an alternative syntax)

   .. code::

      +-----------------------+----+-----------------------------------+
      | Queue                 | Nb | Details                           |
      +=======================+====+===================================+
      | big_jobs_few_tasks    | 2  | Non igitur potestis               |
      |                       |    | voluptate omnia dirigentes        |
      +-----------------------+----+-----------------------------------+
      | small_jobs_many_tasks | 10 |                                   |
      +-----------------------+----+-----------------------------------+
      | lazy_table_injection  | 4  | Videamus animi partes,            |
      |                       |    | quarum est conspectus illustrior; |
      +-----------------------+----+-----------------------------------+

Some maths
-----------
Just to play with maths: :math:`\sigma (x) = \frac{1}{1 + e^{-1}}`, Sigmoid
function used in word2vec model

.. tab:: Sigmoid Math

  .. math::

    \sigma (x) = \frac{1}{1 + e^{-1}}

  In line math: :math:`e^{i\pi} + 1 = 0` from Euler

.. tab:: Maths (use Tex notation)

  .. code::

     .. math::

        \sigma (x) = \frac{1}{1 + e^{-1}}

     In line math: :math:`e^{i\pi} + 1 = 0` from Euler

Links
------

External Links
~~~~~~~~~~~~~~~~
.. tab:: External Links

  - To link to an **external URL** just write the URL sphinx will detect it as a link:
    : e.g. ``https://www.mazars.com``:  https://www.mazars.com

    - If you want to name the link use the ```LINK NAME <URL>`__`` pattern (write *LINK
      NAME <URL>* inside backquotes ending with double underscores) e.g. like
      `Mazars <https://www.mazars.com>`__

.. tab:: External Links -- code

  .. code::

    - To link to an **external URL** just write the URL sphinx will detect it as a link:
      : e.g. ``https://www.mazars.com``:  https://www.mazars.com

      - If you want to name the link use the ```LINK NAME <URL>`__`` pattern (write *LINK
        NAME <URL>* inside backquotes ending with double underscores) e.g. like
        `Mazars <https://www.mazars.com>`__

Links to rst with :doc:
~~~~~~~~~~~~~~~~~~~~~~~~
.. tab:: links to rst with :doc:

  - To link to **some other rst document** we use the ``:doc:`` role followed by
    path to rst file (without ``.rst``) into backquotes:
    ``:doc:`/src/path/to_the_rst_file``` e.g.
    :doc:`/src/sphinx_tutorial/mermaid_syntax_demo`

    - We can rename the link as ``LINK NAME`` with the same pattern as external URLs:
      ``:doc:`LINK NAME </src/path/to_the_rst_file>``` e.g. :doc:`Mermaid exemples
      </src/sphinx_tutorial/mermaid_syntax_demo>`

    - .. attention::

         For ``:doc:`` role, the link to e.g. ``mermaid_syntax_demo.rst`` has to start by
         an absolute path starting with a slash ``/src/sphinx_tutorial/...`` and should
         not have the ``.rst`` extention

.. tab:: links to rst with :doc: -- code

  .. code::

    - To link to **some other rst document** we use the ``:doc:`` role followed by
      path to rst file (without ``.rst``) into backquotes:
      ``:doc:`/src/path/to_the_rst_file``` e.g.
      :doc:`/src/sphinx_tutorial/mermaid_syntax_demo`

      - We can rename the link as ``LINK NAME`` with the same pattern as external URLs:
        ``:doc:`LINK NAME </src/path/to_the_rst_file>``` e.g. :doc:`Mermaid exemples
        </src/sphinx_tutorial/mermaid_syntax_demo>`

      - .. attention::

        For ``:doc:`` role, the link to e.g. ``mermaid_syntax_demo.rst`` has to start by an
        absolute path starting with a slash ``/src/sphinx_tutorial/...`` and should not
        have the ``.rst`` extention

Links to a specific Chapter with :ref:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. tab:: Links to a specific chapter

  - To **link to some specific chapter** use the ``:ref:`` role followed by
    *PATH/TO/RST_FILE:Chapter title* into backquotes:
    ``:ref:`src/path/rst_file:Chapter name``` e.g.
    :ref:`src/sphinx_tutorial/sphinx_syntax_tutorial:Some maths`

    - .. warning::

        For ``:ref:`` role the path should not start with ``/``, we write
        ``src/sphinx_tutorial`` not ``/src/sphinx_tutorial``

    - If you want to name the link replace the ``PATH/TO/RST_FILE:chapter_name`` with
      ``LINK NAME <PATH/TO/RST_FILE:Chapter name>`` e.g. :ref:`Math exemples
      <src/sphinx_tutorial/sphinx_syntax_tutorial:Some maths>` or :ref:`link to the
      *sequenceDiagram* chapter in in mermaid_syntax_demo
      <src/sphinx_tutorial/mermaid_syntax_demo:sequenceDiagram>`

.. tab:: Links to specific chapter -- code

  .. code::

    - To **link to some specific chapter** use the ``:ref:`` role followed by
      *PATH/TO/RST_FILE:Chapter title* into backquotes:
      ``:ref:`src/path/rst_file:Chapter name``` e.g.
      :ref:`src/sphinx_tutorial/wiki_syntax_demo:Some maths`

      - .. warning::

          For ``:ref:`` role the path should not start with ``/``, we write
          ``src/sphinx_tutorial`` not ``/src/sphinx_tutorial``

      - If you want to name the link replace the ``PATH/TO/RST_FILE:chapter_name`` with
        ``LINK NAME <PATH/TO/RST_FILE:Chapter name>`` e.g. :ref:`Math exemples
        <src/sphinx_tutorial/wiki_syntax_demo:Some maths>` or :ref:`link to the
        sequenceDiagram in mermaid_syntax_demo
        <src/sphinx_tutorial/mermaid_syntax_demo:sequenceDiagram>`

.. note::

  - Sphinx can be used with `markdown <https://spec.commonmark.org/0.30>`_ too but is
    not recomendend neither as powerfull as restructuredtext is.

Add Bibliography
----------------

Sphinx allow to manage BibTeX bibliography the de-facto standard in research.

.. tab:: add BibTeX to ``conf.py``

  Add ``sphinxcontrib.bibtex`` to ``conf.py extensions`` and point bibtex_bibfiles to
  your ``refs.bib``:

  .. code:: python

    # pip install sphinxcontrib.bibtex
    extensions = ['sphinx.ext.graphviz', ...]
    bibtex_bibfiles = ['refs.bib']

.. tab:: Create a bib file

  At the same level than ``conf.py`` add a ``resfs.bib`` with all your bibliography in
  BibTeX format::

    doc$ ls -l
    -rw-rw-r-- 1 luis luis 1,2K déc.   7 12:15 Makefile
    -rw-rw-r-- 1 luis luis  179 déc.   7 12:15 index.rst
    -rw-rw-r-- 1 luis luis 2,2K déc.   7 12:15 conf.py
    -rw-rw-r-- 1 luis luis  30K déc.  11 17:11 refs.bib
    ...
    doc$
    doc$ cat refs.bib
    @article{khurana_natural_2022,
        title = {Natural language processing: state of the art, current trends and challenges},
        issn = {1573-7721},
        shorttitle = {Natural language processing},
        url = {https://doi.org/10.1007/s11042-022-13428-4},
        ...
    doc$

.. tab:: Cite articles

  :cite:p:`khurana_natural_2022` provide a clear NLP state of the art 2022, we can refer
  to this article with with footnotes :footcite:p:`khurana_natural_2022` too.

  The above paragraphe is provided by the following code:

  .. code::

    :cite:p:`khurana_natural_2022` provide a clear NLP state of the art 2022, we can
    refer to this article with with footnotes :footcite:p:`khurana_natural_2022` too.


.. tab:: Add a Bibliography section

  Add a ``bibliography::`` directive at the end of your document::

    Bibliography
    =============

    .. bibliography::

    .. footbibliography::


Bibliography
=============

.. bibliography::

.. footbibliography::
