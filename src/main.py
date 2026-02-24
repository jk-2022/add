import flet as ft

from screens.screens import *
# ================= ENTREPRISE EAU POTABLE - FLET 0.80.5 =================



def main(page: ft.Page):
    page.title = "AquaPure - Eau Potable"
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.LIGHT


    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(HomeView())
        elif page.route == "/products":
            page.views.append(ListProductView())
        elif page.route.startswith("/detail/"):
            pid = int(page.route.split("/")[-1])
            page.views.append(DetailView(pid))
        elif page.route == "/about":
            page.views.append(AboutView())
        elif page.route == "/contact":
            page.views.append(ContactView())

        # page.update()
    page.views.append(HomeView())
    page.on_route_change = route_change
    # page.go("/")


ft.run(main)