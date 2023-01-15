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

project = 'Rapport de stage au laboratoire CNRS du musé de l\'homme'
copyright = '12/12/22 au 16/12/22'
author = 'Mario Belmar Letelier -- Zhou'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.mermaid',
    'sphinxcontrib.bibtex',
    'sphinx.ext.autosectionlabel',
]
bibtex_bibfiles = ['refs.bib']
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'fr'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = "pydata_sphinx_theme"
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [
    'css/custom.css'
]

# -- Options for LaTeX output --------------------------------
title = """Rapport de stage\\newline\\newline\\large au muséum national d'histoire
naturelle\\newline\\ du 12 au 16 décembre"""
# title = "Rapport de stage\\newline\\ au muséum national d'histoire naturelle"
# latex_theme = 'manual'  # 'manual' to make a book, 'howto' to make an article
latex_documents = [('index', 'mario_rapport_stage_umr7206.tex', title, author,
                    'report')]
latex_engine = 'lualatex'

latex_elements = {
  'papersize': 'a4paper',  # 'letterpaper' or 'a4paper'
  'pointsize': '12pt',     # global fontsize, possible values are 10pt, 11pt and 12pt
  'sphinxsetup': 'hmargin={1.5cm,1.5cm}, vmargin={2cm,2cm}',
  'extraclassoptions': 'openany'
  # 'classoptions': ',twocolumn',    # to have two columns
  # 'tableofcontents': '',           # To remove the TOC
  # 'babel' : '\\usepackage[english]{babel}',
  }

