import flet as ft 
from _navbar import NavBar
from navbar import navbar
from footer import footer

class ContactView(ft.View):
    def __init__(self):
        super().__init__()
        self.padding=0
        self.expand=True
        self.scroll=ft.ScrollMode.ALWAYS
        
        self.route="/contact"
        self.controls=[
            NavBar(),
            ft.Container(
                padding=60,
                content=ft.Column(
                    width=500,
                    controls=[
                        ft.Text("Contactez-nous", size=28, weight=ft.FontWeight.BOLD),
                        ft.TextField(label="Nom"),
                        ft.TextField(label="Email"),
                        ft.TextField(label="Message", multiline=True, min_lines=4),
                        ft.Button("Envoyer"),
                    ],
                ),
            ),
            footer(),
        ]
        
    def page_go(self,route):
        self.page.go(route)
