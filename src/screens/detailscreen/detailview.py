import flet as ft 
from _navbar import NavBar
from navbar import navbar
from footer import footer

from donnees import PRODUCTS
from productcard import ProductCard

class DetailView(ft.View):
    def __init__(self, pid:int):
        super().__init__()
        self.padding=0
        self.expand=True
        self.scroll=ft.ScrollMode.ALWAYS
        product = next((p for p in PRODUCTS if p["id"] == pid), None)
  
        self.route=f"/detail/{pid}"
        
        self.controls=[
            NavBar(),
            ft.Container(
                padding=60,
                content=ft.Column(
                    controls=[
                        ft.Text(product["title"], size=32, weight=ft.FontWeight.BOLD),
                        ft.Image(src=product["image"], height=400, fit=ft.BoxFit.COVER),
                        ft.Text(product["desc"], size=18),
                        ft.Button("Retour", on_click=lambda e: self.page.go("/products")),
                    ]
                ),
            ),
            footer(),
        ]
    def page_go(self,route):
        self.page.go(route)