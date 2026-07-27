import reflex as rx
from enum import Enum
from link_bio_1963.styles.colors import Color, TextColor
from link_bio_1963.styles.fonts import Font, FontWeight

#Constants
MAX_WIDTH = "560px"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa-Medium:wght@500&display=swap",
]

#sizes

class Spacer(Enum):
    """Enum for spacer sizes."""
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "2em"

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Spacer.SMALL.value,
        "border_radius": Spacer.MEDIUM.value,
        "background_color": Color.CONTENT.value,
        "_hover": {
            "background_color": Color.SECONDARY.value,
        }
    }
}

title_style = dict(    
    font_family=Font.TITLE.value,
    font_weight=FontWeight.MEDIUM.value,
    width="100%",
    padding_top=Spacer.DEFAULT.value,
    color=TextColor.HEADER.value,
    align="left",    
)


button_title_style = dict(
    font_family=Font.TITLE.value,    
    font_weight=FontWeight.MEDIUM.value,
    font_size=Spacer.DEFAULT.value,
    color=TextColor.HEADER.value,
    
)

button_body_style = dict(
    font_family=Font.DEFAULT.value,    
    font_weight=FontWeight.LIGHT.value,
    font_size=Spacer.MEDIUM.value,
    color=TextColor.BODY.value,
    
)