import reflex as rx
import link_bio_1963.styles.styles as styles

def link_sponsor(imagen: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            alt="Sponsor",
            width="100px",            
        ),
        href=url,
        is_external=True,
    )