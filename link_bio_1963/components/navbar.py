import reflex as rx
from link_bio_1963.styles.styles import Spacer as Spacer
from link_bio_1963.styles.colors import Color
from link_bio_1963.styles.fonts import Font, FontWeight

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "moure",
            rx.text(
                "dev",
                as_="span",
                color=Color.SECONDARY.value,                
            ),
            height="40px",            
            color=Color.PRIMARY.value,
            font_family=Font.LOGO.value,
            FontWeight=FontWeight.MEDIUM.value,
            size="7"                   
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Spacer.LARGE.value,
        padding_y=Spacer.DEFAULT.value,
        z_index="999",
        top="0",
    )