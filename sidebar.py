import flet
from flet import *

class Sidebar(UserControl):

    def __init__(self, app_layout, page):
        super().__init__()
        self.app_layout = app_layout
        self.page = page
        self.top_nav_items = [
            NavigationRailDestination(
                label_content=Text("Boards"),
                label="Boards",
                icon=icons.BOOK_OUTLINED
            ),
            NavigationRailDestination(
                label_content=Text("Membros"),
                label="Members",
                icon=icons.PERSON,
                selected_icon=icons.PERSON
            ),
        ]
        self.top_nav_rail = NavigationRail(
            selected_index=None,
            label_type="all",
            on_change=self.top_nav_change,
            destinations=self.top_nav_items,
            bgcolor=colors.BLUE_GREY,
            extended=True,
            expand=True
        )

    def build(self):
        self.view = Container(
            content=Column([
                Row([
                    Text("Workspace")
                ])
            ])
        )