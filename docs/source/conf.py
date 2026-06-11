# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'NV2 Lab Manual'
copyright = '2026, Alex Ungar'
author = 'Alex Ungar'
release = '0.1'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

myst_enable_extensions = [
    'colon_fence',
]

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'
html_static_path = ['_static']
html_title = "NV2 Lab Manual"
