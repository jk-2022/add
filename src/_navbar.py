import flet as ft

class NavBar(ft.Container):
    def __init__(self):
        super().__init__()
        is_mobile = False
        if is_mobile:
            menu = ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Accueil", 
                    on_click=lambda e: self.page_go_home
                    ),
                    ft.PopupMenuItem(text="Produits", 
                    on_click=lambda e: self.page_go_product
                    ),
                    ft.PopupMenuItem(text="À propos", 
                    on_click=lambda e: self.page_go_about
                    ),
                    ft.PopupMenuItem(text="Contact", 
                    on_click=lambda e: self.page_go_contact
                    ),
                ]
            )
            right = menu
        else:
            right = ft.Row(
                spacing=20,
                controls=[
                    ft.Button("Accueil", 
                    on_click= self.page_go_home
                    ),
                    ft.Button("Produits", 
                    on_click= self.page_go_product
                    ),
                    ft.Button("À propos", 
                    on_click= self.page_go_about
                    ),
                    ft.Button("Contact", 
                    on_click= self.page_go_contact
                    ),
                ],
            )

        
        self.bgcolor="#fcfcfd"
        self.padding=10
        self.content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Container(
                    width=120,
                    padding=0,
                    # bgcolor='white',
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Image(src="logo.png", 
                                    width=40, 
                                    height=40,
                                    fit=ft.BoxFit.FILL
                                    ),
                            ft.Text("ADD", size=22, weight=ft.FontWeight.BOLD, color="#0c42b8")
                        ]
                    )
                    ),
                right,
            ],
        )
    
    async def page_go_home(self,e):
        await self.page.push_route("/")    
    async def page_go_product(self,e):
        await self.page.push_route("/products")    
    async def page_go_about(self,e):
        await self.page.push_route("/about")    
    async def page_go_contact(self,e):
        await self.page.push_route("/contact")    