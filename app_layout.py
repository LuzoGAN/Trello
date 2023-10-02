import flet
from flet import *
from sidebar import Sidebar

class AppLayout(Row):
    def __int__(
            self,
            app,
            page: Page,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        self.togle_nav_rail_button = IconButton(
            icon=icons.ARROW_CIRCLE_LEFT, icon_color=colors.BLUE_GREY_400, selected=False,
            selected_icon=icons.ARROW_CIRCLE_RIGHT, on_click=self.togle_nav_rail_button)
        self.sidebar = Sidebar(self, page)
        self._active_view: Control = Column(Control[
            Text("Active View")
        ], alignment="center", horizontal_alignment="center")
        self.controls = [self.sidebar,
                         self.togle_nav_rail_button, self.active_view]

    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.update()

    def toggle_nav_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.togle_nav_rail_button.selected = not self.togle_nav_rail_button.selected
        self.page.update()