# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'contamination'
copyright = '2022, Mario & Baptiste'
author = 'Mario \& Baptiste'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinxcontrib.mermaid'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'INSTALL.rst', 'slides']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for LaTeX output --------------------------------
latex_engine = 'xelatex'
title = "La contaminacion \\newline\\newline\\large y como luchar contra ella !"
latex_documents = [('index', 'contaminacion.tex', title, author, 'manual')]
latex_elements = {
  'papersize': 'a4paper',  # 'letterpaper' or 'a4paper'
  'pointsize': '10pt',     # global fontsize, possible values are 10pt, 11pt and 12pt
  'sphinxsetup': 'hmargin={1.5cm,1.5cm}, vmargin={2cm,2cm}',
  'preamble': '\setcounter{tocdepth}{2}',
  # 'classoptions': ',twocolumn',    # to have two columns
  # 'tableofcontents': '',           # To remove the TOC
  }
latex_theme = 'howto'  # 'manual' to make a book, 'howto' to make an article

