# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# +++ START: ADD THESE LINES +++
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
# +++ END: ADD THESE LINES +++


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'test_julia'
copyright = '2025, JuanDiego Prochazka'
author = 'JuanDiego Prochazka'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'breathe',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


# Path to your Doxygen XML output
breathe_projects = {
    "test_julia": "../doxygen/xml"  # adjust path if your xml folder is elsewhere
}
breathe_default_project = "test_julia"

intersphinx_mapping = {
    'julia': ('/home/juan-prochazka/Desktop/Thesis/test_julia/test_julia/docs/juliadocs_build', 
              '/home/juan-prochazka/Desktop/Thesis/test_julia/test_julia/docs/juliadocs_build/objects.inv')
}

# Optional: nicer theme
html_theme = "sphinx_rtd_theme"