import flet as ft

def footer():
    return ft.Row(
        # expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                bgcolor="#e0f2fe",
                padding=30,
                expand=True,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text("© 2026 AquaPure - Production d'eau potable"),
                        ft.Text("Qualité • Hygiène • Confiance"),
                    ],
                ),
            )
        ]
    )