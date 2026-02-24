import flet as ft 
from _navbar import NavBar
from navbar import navbar
from footer import footer

class AboutView(ft.View):
    def __init__(self):
        super().__init__()
        self.padding=0
        self.route="/about"
        self.expand=True
        self.scroll=ft.ScrollMode.ALWAYS
        
        self.controls=[
            NavBar(),
            ft.Container(
                padding=60,
                expand=1,
                content=ft.Column(
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Text(
                            "AquaPure est une entreprise spécialisée dans la production et la distribution d'eau potable certifiée.\n"
                            "Nous garantissons qualité, hygiène et respect des normes sanitaires.",
                            size=20,
                        ),
                    ]
                )
            ),
            footer(),
        ]
    
    def page_go(self,route):
        self.page.go(route)