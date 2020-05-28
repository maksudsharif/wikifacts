"""Sphinx configuration."""
from datetime import datetime


project = "wikifacts"
author = "Maksud Sharif"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx_autodoc_typehints"]
