"""
__init__.py
Ian Kollipara
2022.10.03

Vignette is a Website for WWII pilots and Aircraft.
"""

# Imports
from fastapi import FastAPI


def create_app():
    """Create and bootstrap the core application.

    This returns a FastAPI instance.
    """

    app = FastAPI()

    return app
