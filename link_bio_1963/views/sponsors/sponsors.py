import reflex as rx
from link_bio_1963.components.title import title
from link_bio_1963.components.link_sponsor import link_sponsor
from link_bio_1963.styles.styles import Spacer as Spacer

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.hstack(
            link_sponsor("elgato.png", "https://www.google.com/finance/beta?utm_source=pwa&lfhs=2"),
            link_sponsor("mvp.png", "https://www.google.com/finance/beta?utm_source=pwa&lfhs=2"),
            spacing="5",
        ),
        width="100%",
        align="start",
    )