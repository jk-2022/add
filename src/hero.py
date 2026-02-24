import flet as ft 

def Hero():
    return ft.Stack(
        controls=[
            hero_image,
            ft.Container(bgcolor="#00000066", width=float("inf"), height=500),
            ft.Container(
                alignment=ft.Alignment.CENTER,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("AquaPure",
                                size=45,
                                weight=ft.FontWeight.BOLD,
                                color="white"),
                        ft.Text("Une eau pure, saine et accessible à tous",
                                size=20,
                                color="white"),
                        ft.Button("Voir nos produits", on_click=lambda e: page.go("/products")),
                    ],
                ),
            ),
        ]
    )