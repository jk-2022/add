import asyncio
import flet as ft 
import flet_webview as fwv
from donnees import PRODUCTS
from _navbar import NavBar
from footer import footer
from honoraire import honoraire
from productcard import ProductCard
from .section_text import SectionText1, SectionText2, SectionText3

# MAP="https://maps.app.goo.gl/4iHbZV2yPnv6GLvp9"
# MAP="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1647.3184497032305!2d0.19707873509258894!3d10.887174836306746!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x11d5455c1dfd1357%3A0x6f6cb269815effa9!2sDirection%20r%C3%A9gionale%20de%20l&#39;Eau%20et%20de%20l&#39;Hydraulique%20villageoise%20Dapaong!5e0!3m2!1sfr!2stg!4v1771851709790!5m2!1sfr!2stg"

class HomeView(ft.View):
    def __init__(self, route="/"):
        super().__init__()
        self.padding=0
        self.spacing=0
        self.expand=True
        self.navbar_=NavBar()
        
        # selfmap_view = fwv.WebView(
        #     url=MAP,
        #     expand=True,
        # )
        
        self.slider_images = [
        "banne1.jpg",
        "banne2.jpg",
        "banne3.jpg",
        ]

        self.slider_index = 0
        self.hero_image = ft.Image(
            src=self.slider_images[0],
            fit=ft.BoxFit.COVER,
            width=float("inf"),
            height=500,
            opacity=1,
        )

        self.hero = ft.Stack(
            controls=[
                self.hero_image,
                ft.Container(bgcolor="#1A141466", 
                             width=float("inf"),
                             height=500,
                             content=ft.Text("Nous vous apportons bien plus que la vie !",
                                             size=30, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                             alignment=ft.Alignment.CENTER
                             ),
                ft.Container(
                    alignment=ft.Alignment.CENTER,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text("La TOGOLAISE",
                                    size=45,
                                    weight=ft.FontWeight.BOLD,
                                    color="white"),
                            ft.Text("Une eau pure, saine et accessible à tous",
                                    size=20,
                                    color="white"),
                            ft.Button("Voir nos produits", on_click=lambda e: self.page.go("/products")),
                        ],
                    ),
                ),
            ]
        )
        
        self.controls=[
            self.navbar_,
            ft.Container(
                expand=True,
                # bgcolor="blue",
                content=ft.Column(
                    expand=True,
                    scroll=ft.ScrollMode.ALWAYS,
                    on_scroll=self.on_scroll_to,
                    controls=[
                        self.hero,
                        ft.Row(
                            expand=True,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            controls=[
                                ft.Column(
                                        expand=1,
                                        controls=[
                                            ft.Container(
                                                alignment=ft.Alignment.CENTER,
                                                expand=True,
                                                # bgcolor="blue",
                                                content=ft.Column(
                                                    expand=True,
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    controls=[
                                                        ft.Column(
                                                                [
                                                                    ft.IconButton(icon=ft.Icons.CALL),
                                                                    ft.IconButton(icon=ft.Icons.FACEBOOK),
                                                                    ft.IconButton(icon=ft.Icons.MAIL),
                                                                    ft.IconButton(icon=ft.Icons.SHARE),
                                                                ]
                                                            ),
                                                    ]
                                                )
                                                ),
                                        ]
                                    ),
                                ft.Container(
                                    expand=3,
                                    content=ft.Column(
                                        spacing=20,
                                        controls=[
                                            SectionText1(),
                                            SectionText2(),
                                            SectionText3(),
                                            ft.Text("Nos Formats Disponibles", size=45, weight=ft.FontWeight.BOLD),
                                            ft.ResponsiveRow(
                                                columns=6,
                                                controls=[ProductCard(product=p) for p in PRODUCTS]
                                            ),
                                            honoraire(),
                                            # selfmap_view,
                                        ]
                                    )
                                ),
                                ft.Container(
                                    expand=1
                                ),
                            ]
                            ),
                    ]
                ),
            ),
            footer(),
        ]
    def did_mount(self):
        
        self.page.run_task(self.auto_slider)
        

    async def auto_slider(self):
        self.slider_index
        while True:
            await asyncio.sleep(4)
            self.slider_index = (self.slider_index + 1) % len(self.slider_images)
            self.hero_image.opacity = 0
            # self.hero_image.update()
            await asyncio.sleep(0.5)
            self.hero_image.src = self.slider_images[self.slider_index]
            self.hero_image.opacity = 1
            # self.hero_image.update()

        
    def on_scroll_to(self, e: ft.OnScrollEvent):
        if e.pixels > 50:
            self.navbar_.bgcolor = "#0077b6"
        if e.pixels > 100:
            self.navbar_.visible=False
        else:
            self.navbar_.bgcolor = "transparent"
            self.navbar_.visible=True

        self.navbar_.update()
