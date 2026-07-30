import reflex as rx

config = rx.Config(
    app_name="link_bio_1963",
    #la api solo es en caso de desplegar el backend en servidor distinto
    api_url="https://linkbio-production-7687.up.railway.app/",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin()
    ]
)