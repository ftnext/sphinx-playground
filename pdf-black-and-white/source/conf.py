# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Black and White PDF'
copyright = '2024, nikkie'
author = 'nikkie'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for LaTeX PDF output --------------------------------------------
PREAMBLE = r"""
% ハイパーリンクに色がつかない。ただし水色の線で囲まれる
% \hypersetup{colorlinks=false}

% ハイパーリンクに色がつかず、囲みもない
\hypersetup{hidelinks}
"""
latex_elements = {
    "preamble": PREAMBLE
}
