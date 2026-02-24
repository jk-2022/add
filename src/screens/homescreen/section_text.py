import flet as ft 


def SectionText1():
    return ft.Container(
        content=ft.Column(
            spacing=5,
            controls=[
                ft.Text("Production et distribution d'eau potable", weight=ft.FontWeight.BOLD, size=42),
                ft.Text("Produire et distribuer chaque jour une eau de qualité sanitaire irréprochable à des millions de personnes ou fournir aux entreprises les eaux, spécifiques ou non, indispensables à leur activité sont des missions qui exigent l’excellence.", weight=ft.FontWeight.W_300, size=25),
            ]
        )
    )
    
def SectionText2():
    return ft.Container(
        content=ft.Column(
            spacing=5,
            controls=[
                ft.Text("Des solutions de traitement adaptées", weight=ft.FontWeight.BOLD, size=42),
                ft.Text("Les traitements conçus et opérés par ADD garantissent la protection de la santé des populations, la productivité des industriels et leur meilleure intégration dans les communautés locales, la préservation de l’environnement et la réduction des empreintes carbone et eau.", weight=ft.FontWeight.W_300, size=25),
            ]
        )
    )   
     
def SectionText3():
    return ft.Container(
        content=ft.Column(
            spacing=5,
            controls=[
                ft.Text("Une  traçabilité de l’eau garantie", weight=ft.FontWeight.BOLD, size=42),
                ft.Text("Afin d'assurer la préservation de  la qualité de l’eau potable,  de la sortie de l’usine à sa livraison chez le consommateur, ADD a mis au point des méthodes de mesure et d’analyse innovants, utilise des réseaux communicants et des systèmes d’information permettant de piloter finement l’exploitation du réseau. ADD a par exemple développé des sondes qui permettent de suivre en temps réel des différents aspects de la qualité de l’eau dans les réseaux de distribution.", weight=ft.FontWeight.W_300, size=25),
            ]
        )
    )