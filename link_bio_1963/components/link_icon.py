import reflex as rx
from link_bio_1963.styles import styles as styles

def link_icon(url: str, image: str) -> rx.Component:
    return rx.link(
        rx.image(src=image,
                 width="20px",
                 height="auto",
                 alt="imagen del logotipo de la plicación.",
                 ),
        href=url,
        is_external=True,
    )