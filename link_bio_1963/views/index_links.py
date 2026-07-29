import reflex as rx
from link_bio_1963.components.link_button import link_button
from link_bio_1963.components.title import title
from link_bio_1963.routes import Route

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(title="Cursos", body="Este es el enlace para la página de cursos", url=Route.COURSES.value, image="icons/instagram.svg", is_external=False),
        link_button("Twitch", "Este es el enlace para Twitch", "https://twitch.tv", "icons/twitch.svg"),
        link_button("YouTube", "Este es el enlace para YouTube", "https://youtube.com", "icons/youtube.svg"),        
        link_button("Twitter", "Este es el enlace para Twitter", "https://twitter.com", "icons/x.svg"),

        title("Comunidad"),
               link_button("Twitch", "Este es el enlace para Twitch", "https://twitch.tv", "icons/twitch.svg"),
                       link_button("YouTube", "Este es el enlace para YouTube", "https://youtube.com", "icons/youtube.svg"),
                       link_button("Instagram", "Este es el enlace para Instagram", "https://instagram.com", "icons/instagram.svg"),
                       link_button("Twitter", "Este es el enlace para Twitter", "https://twitter.com", "icons/x.svg"),

        title("Contacto"),
                link_button("MyPublicInbox", "Respuesta rápida y con preferencia", "https://twitch.tv", "icons/twitch.svg"),
                link_button("Email", "Este es el enlace para YouTube", "https://youtube.com", "icons/email.svg"),
        align="center",
        width="100%",        
    )