import flet as ft


class ProductCard(ft.Card):
    def __init__(self, product):
        super().__init__()
        # self._page=page
        self.product=product
        self.col={"xs": 12, "sm": 6, "md": 3}
        self.padding=15
        self.content=ft.Container(
            bgcolor="white",
            on_hover = self.hover,
            on_click=self.go_detail,
            ink=True,
            border_radius=20,
            shadow=ft.BoxShadow(blur_radius=10),
            content=ft.Column(
                    controls=[
                        ft.Container(
                            height=200,
                            image=ft.DecorationImage(
                                src=product["image"],
                                fit=ft.BoxFit.FILL
                            )
                            ),
                        ft.Container(
                            padding=15,
                            content=ft.Column(
                                controls=[
                                    ft.Text(product["title"], size=18, weight=ft.FontWeight.BOLD),
                                    ft.Text(product["desc"]),
                                    ft.Button("Détails",on_click=self.go_detail
                                        ),
                                ]
                            )
                            )
                                
                        ]
                        ),
                    )

    def hover(self,e):
        self.content.scale = 1.05 if self.content.scale==1 else 1
        self.content.update()

    async def go_detail(self,e):
        await self.page.push_route(f"/detail/{self.product['id']}")