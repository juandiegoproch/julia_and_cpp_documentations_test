import os
import sys
from pathlib import Path

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'test_julia'
copyright = '2025, Juan Diego Prochazka'
author = 'Juan Diego Prochazka'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "breathe",
    "sphinx.ext.intersphinx",
    "myst_parser",
]

breathe_projects = {
    "libadd": "../doxy_docs/doxygen/xml"
}
breathe_default_project = "libadd"

#julia_docs_path = Path(__file__).parent.parent / "julia_docs/build"

#intersphinx_mapping = {
#    "julia": (None, str(julia_docs_path / "objects.inv")),
#}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
