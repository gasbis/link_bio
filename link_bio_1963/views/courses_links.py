import reflex as rx
from link_bio_1963.components.link_button import link_button
from link_bio_1963.components.title import title
import link_bio_1963.constants as const

def courses_links() -> rx.Component:
    return rx.vstack(
        title("Cursos gratis"),
        link_button(
            title="Retos de programación",
            body="Este es el enlace para la página de cursos", url=const.CODE_CHALLENGES_URL,
            image="icons/code.svg",
            ),
        link_button(
            title="Python desde cero",
            body="Este es el enlace para la página de cursos", url=const.PYTHON_COURSE_URL,
            image="icons/code.svg",
            ),
        link_button(
            title="Git y Git Hub",
            body="Este es el enlace para la página de cursos", url=const.GIT_COURSE_URL,
            image="icons/git.svg",
            ),
        link_button(
            title="SQL y Bases de datos",
            body="Este es el enlace para la página de cursos", url=const.SQL_COURSE_URL,
            image="icons/code.svg",
            ),
        title("Mucho más en"),
        link_button("Twitch", "Este es el enlace para Twitch", "https://twitch.tv", "icons/twitch.svg"),
        link_button("YouTube", "Este es el enlace para YouTube", "https://youtube.com", "icons/youtube.svg"),
        link_button("Instagram", "Este es el enlace para Instagram", "https://instagram.com", "icons/instagram.svg"),
        link_button("Twitter", "Este es el enlace para Twitter", "https://twitter.com", "icons/x.svg"),  
        align="center",
        width="100%",        
    )