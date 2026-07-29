import reflex as rx
from link_bio_1963.components.link_icon import link_icon
from link_bio_1963.styles import styles as styles
from link_bio_1963.components.info_text import info_text
from link_bio_1963.styles.colors import TextColor, Color

def header(details = True) -> rx.Component:
    return rx.stack(
        rx.hstack(
            rx.avatar(
            src="avatar.jpg",
            size="6",
            radius="full",
            padding="2px",
            border="4px solid",
            border_color=Color.PRIMARY.value,
            ),
            rx.vstack(
                rx.heading("Brais Moure",
                           size="4",
                           color=TextColor.HEADER.value,
                           ),
                rx.text("@mouredev",
                        margin_top="0px !important",
                        color=TextColor.BODY.value),
                rx.hstack(
                link_icon("https://twitter.com/mouredev", "icons/x.svg"),
                link_icon("https://github.com/mouredev", "icons/github.svg"),
                link_icon("https://www.youtube.com/@mouredev", "icons/youtube.svg"),
                ),
            ),
        spacing="7",   

        ),
        #COndicional para que esta parte salga solo en la página principal
        rx.cond(
            details,
            rx.flex(
                info_text("+13", "años de experiencia"),
                rx.spacer(),
                info_text("+13", "años de experiencia"),
                rx.spacer(),
                info_text("+13", "años de experiencia"),
                width="100%",
            ),      
        ),
        rx.cond(
            details,    
            rx.text("Soy ingeniero de software y divulgador. Te enseño programación e inteligencia artificial desde cero. Aquí podrás encontrar todos mis enlaces de interés Soy ingeniero de software y divulgador. Te enseño programación e inteligencia artificial desde cero. Aquí podrás encontrar todos mis enlaces de interés¡Bienvenid@!",
            ),
        ),
        width="100%",
        color=TextColor.BODY.value,
        spacing="6",
        direction="column",        
        align="start",        
    )