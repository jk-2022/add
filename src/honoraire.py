import flet as ft 

def honoraire():
    return ft.Container(
        expand=True,
        content=ft.Column(
            expand=True,
            spacing=0,
            controls=[
                ft.Text("Nos Honoraires", size=42, weight=ft.FontWeight.BOLD),
                ft.DataTable(
                    expand=True,
                    columns=[
                        ft.DataColumn(label=ft.Text("Jours"), expand=True),
                        ft.DataColumn(label=ft.Text(""), expand=True),
                        ft.DataColumn(label=ft.Text(""), expand=True),
                    ],
                    rows=[
                        ft.DataRow(
                            expand=True,
                            cells=[
                                ft.DataCell(ft.Text("Lundi"), expand=True),
                                ft.DataCell(ft.Text("7h-12h"), expand=True),
                                ft.DataCell(ft.Text("14h-17h"), expand=True),
                            ],
                        ),
                        ft.DataRow(
                            expand=True,
                            cells=[
                                ft.DataCell(ft.Text("Mardi"), expand=True),
                                ft.DataCell(ft.Text("7h-12h"), expand=True),
                                ft.DataCell(ft.Text("14h-17h"), expand=True),
                            ],
                        ),
                        ft.DataRow(
                            expand=True,
                            cells=[
                                ft.DataCell(ft.Text("Mercredi"), expand=True),
                                ft.DataCell(ft.Text("7h-12h"), expand=True),
                                ft.DataCell(ft.Text("14h-17h"), expand=True),
                            ],
                        ),
                        ft.DataRow(
                            expand=True,
                            cells=[
                                ft.DataCell(ft.Text("Jeudi"), expand=True),
                                ft.DataCell(ft.Text("7h-12h"), expand=True),
                                ft.DataCell(ft.Text("14h-17h"), expand=True),
                            ],
                        ),
                        ft.DataRow(
                            expand=True,
                            cells=[
                                ft.DataCell(ft.Text("Vendredi"), expand=True),
                                ft.DataCell(ft.Text("7h-12h"), expand=True),
                                ft.DataCell(ft.Text("14h-17h"), expand=True),
                            ],
                        ),
                        ft.DataRow(
                            expand=True,
                            cells=[
                                ft.DataCell(ft.Text("Samedi"), expand=True),
                                ft.DataCell(ft.Text("7h-12h"), expand=True),
                                ft.DataCell(ft.Text("14h-17h"), expand=True),
                            ],
                        ),
                        ft.DataRow(
                            expand=True,
                            cells=[
                                ft.DataCell(ft.Text("Dimanche"), expand=True),
                                ft.DataCell(ft.Text(""), expand=True),
                                ft.DataCell(ft.Text("fermé"), expand=True),
                            ],
                        ),
                    ],
                )
            ]
        )
    )
    