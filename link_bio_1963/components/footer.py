import reflex as rx
import datetime
from link_bio_1963.styles.colors import TextColor

def footer() -> rx.Component:
    return rx.stack(
        rx.image(src="favicon.ico", alt="icono. Una 'm' entre llaves."),
        rx.link(f"© 2014-{datetime.date.today().year} Mouredev by Brais Moure v3.",
        href="https://mouredev.com",
        is_external=True,
        size="2",
        color=TextColor.FOOTER.value,
        ),
        rx.text(
            "BUILDING SOFTWARE WITH 🖤 FROM GALICIA TO THE WORLD.",
            size="2",
            ),
        direction="column",
        align="center",
        color=TextColor.FOOTER.value,        
    )