import flet as ft 
from _navbar import NavBar
from footer import footer

from donnees import PRODUCTS
from productcard import ProductCard

class ListProductView(ft.View):
    def __init__(self, route= "/products"):
        super().__init__()
        self.padding=0
        self.expand=True
        self.scroll=ft.ScrollMode.ALWAYS
        self.controls=[
            NavBar(),
            ft.Container(
                padding=50,
                content=ft.ResponsiveRow(
                    controls=[ProductCard(product=p) for p in PRODUCTS]
                ),
            ),
            footer(),
        ]
        
    def go_detail(self,route):
        self.page.go(route)
    
    def page_go(self,route):
        self.page.go(route)
