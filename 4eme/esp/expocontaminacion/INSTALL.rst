Install
========
::

  $ pip install hovercraft sphinx furo
  $ git add conf.py index.rst Makefile 
  $ rm make.bat 
  $ vim conf.py     # replace theme with furo 
  $ mkdir src
  $ mkdir src/images
  $ git mv expo_contaminacion.rst src/
  $ vim index.rst   # add to TOC src/expo_contaminacion.rst
  $ make html
  $ firefox _build/html/index.html

