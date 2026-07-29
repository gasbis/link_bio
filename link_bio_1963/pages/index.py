import reflex as rx
from rxconfig import config
from link_bio_1963.components import navbar
from link_bio_1963.components import footer
from link_bio_1963.views import header
from link_bio_1963.views import index_links
import link_bio_1963.styles.styles as styles
from link_bio_1963.views import sponsors
import link_bio_1963.utils as utils

@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta,
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar.navbar(),
        rx.center(
            rx.vstack(        
                header.header(),
                index_links.links(),
                sponsors.sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                align="center",
                margin_y=styles.Spacer.LARGE
            ),
        ),
        footer.footer(),
        padding_bottom=styles.Spacer.LARGE.value,
        padding_x=styles.Spacer.MEDIUM.value,
    )