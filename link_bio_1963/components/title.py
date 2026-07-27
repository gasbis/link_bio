import reflex as rx
from link_bio_1963.styles import styles

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="5",
        style=styles.title_style,

    )