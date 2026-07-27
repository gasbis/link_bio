"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from link_bio_1963.components import navbar
from link_bio_1963.components import footer
from link_bio_1963.views.header import header
from link_bio_1963.views.links import links
import link_bio_1963.styles.styles as styles
from link_bio_1963.views.sponsors import sponsors
class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.box(
        navbar.navbar(),
        rx.center(
            rx.vstack(        
                header.header(),
                links.links(),
                sponsors.sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                align="center",
                margin_y=styles.Spacer.LARGE
            ),
        ),
        footer.footer(),
        padding_bottom=styles.Spacer.LARGE.value,
        padding_x=styles.Spacer.MEDIUM.value,
    )
    




app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
)
app.add_page(
    index,
    title="MoureDev | Te enseño programación y desarrollo de software",
    description="Soy ingeniero de software y divulgador. Te enseño programación e inteligencia artificial desde cero. Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!",
    image="avatar.jpg",
)
