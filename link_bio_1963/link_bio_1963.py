"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import link_bio_1963.styles.styles as styles
from link_bio_1963.pages.index import index
from link_bio_1963.pages.courses import courses



app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
