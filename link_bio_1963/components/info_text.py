import reflex as rx
from link_bio_1963.styles.colors import TextColor, Color

def info_text(title: str, body: str) -> rx.Component:
    return rx.text(title,
                    rx.text(f" {body}",
                    as_="span",
                    color=TextColor.BODY.value,
                    size="2"),
                    color=Color.PRIMARY.value,   
                    size="3"             
                    ),
    