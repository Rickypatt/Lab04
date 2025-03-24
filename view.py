import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self._btnSpell = None
        self._frase = None
        self._ddModality = None
        self._ddLingua = None
        self._textOut = None
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here

        self._ddLingua = ft.Dropdown(label= "Lingua",
                         hint_text= "Seleziona lingua",
                         options=[ft.dropdown.Option("english"), ft.dropdown.Option("spanish"),ft.dropdown.Option("italian")],
                         width = self.page.width)

        self._ddModality = ft.Dropdown(label= "Modalità",
                                       hint_text= "Seleziona modalità",
                                       options=[ft.dropdown.Option("Default"), ft.dropdown.Option("Linear"),
                                                ft.dropdown.Option("Dichotomic")],
                                       width = 200)

        self._frase = ft.TextField(label= "Frase",
                                   hint_text= "Inserisci la frase da tradurre",
                                   width = 450)

        self._btnSpell = ft.ElevatedButton("Spell Check",
                                           on_click = self.__controller.handleSpell)

        row1 = ft.Row(controls = [self._ddLingua], alignment=ft.MainAxisAlignment.START)
        row2 = ft.Row(controls=[self._ddModality,self._frase,self._btnSpell], alignment=ft.MainAxisAlignment.START)
        self._textOut = ft.ListView(expand=True)
        self.page.add(row1, row2, self._textOut)
        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
