import flet as ft

def navbar(page_go):
    is_mobile = False

    if is_mobile:
        menu = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Accueil", 
                on_click=lambda e: page_go("/")
                ),
                ft.PopupMenuItem(text="Produits", 
                on_click=lambda e: page_go("/products")
                ),
                ft.PopupMenuItem(text="À propos", 
                on_click=lambda e: page_go("/about")
                ),
                ft.PopupMenuItem(text="Contact", 
                on_click=lambda e: page_go("/contact")
                ),
            ]
        )
        right = menu
    else:
        right = ft.Row(
            spacing=20,
            controls=[
                ft.Button("Accueil", 
                on_click=lambda e: page_go("/")
                ),
                ft.Button("Produits", 
                on_click=lambda e: page_go("/products")
                ),
                ft.Button("À propos", 
                on_click=lambda e: page_go("/about")
                ),
                ft.Button("Contact", 
                on_click=lambda e: page_go("/contact")
                ),
            ],
        )

    return ft.Container(
        bgcolor="#fcfcfd",
        padding=10,
        content=ft.Row(
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
        ),
    )