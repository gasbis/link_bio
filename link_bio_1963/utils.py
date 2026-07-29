import reflex as rx


#común
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


preview="https://moure.dev/preview.jpg"

_meta=[
    {"name": "og:type", "content": "website"},    
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@mouredev"},    
]

#index
index_title="MoureDev | Te enseño programación y desarrollo de software"
index_description="Soy ingeniero de software y divulgador. Te enseño programación e inteligencia artificial desde cero. Aquí podrás encontrar todos mis enlaces de interés ¡Bienvenid@!"
index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

#courses
courses_title="MoureDev | Cursos gratis"
courses_description="Algunos cursos actuales"
courses_meta = [
    {"name": "og:title", "content": courses_title},
    {"name": "og:description", "content": courses_description},
]
courses_meta.extend(_meta)


