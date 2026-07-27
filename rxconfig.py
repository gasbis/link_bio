import reflex as rx

config = rx.Config(
    app_name="link_bio_1963",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin()
    ]
)