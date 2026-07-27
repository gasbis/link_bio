import reflex as rx
from link_bio_1963.styles import styles as styles

def link_button(title: str, body: str, url: str, image: str) -> rx.Component:

   return  rx.link(
        rx.button(
           rx.hstack(
              rx.image(src=image,
                     width="20px",
                     height="auto",
                     alt="imagen del logotipo de la aplicación."
                  ),
              rx.vstack(
                 rx.text(title, style=styles.button_title_style),
                 rx.text(body, style=styles.button_body_style),
                 spacing="0",
              ),  
              align="center",            
           ),
        ),
        href=url,
        is_external=True,
        width="100%",
        )