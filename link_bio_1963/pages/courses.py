import reflex as rx
from link_bio_1963.components import navbar
from link_bio_1963.components import footer
from link_bio_1963.views import header
from link_bio_1963.views import courses_links
import link_bio_1963.styles.styles as styles
from link_bio_1963.views import sponsors
import link_bio_1963.utils as utils
from link_bio_1963.routes import Route


@rx.page(
    route=Route.COURSES.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta,
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar.navbar(),
        rx.center(
            rx.vstack(        
                header.header(details=False),
                courses_links.courses_links(),
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