from . import pygame_gui as ui
from .components.stacked_page import StackedPageView
from .pages.armor import ArmorPage
from .pages.menu import MainMenu


class Main(ui.Main):
    def __init__(self):
        super().__init__((1280, 800), caption='PyLabelRoboMaster', icon='./resources/icon.png')

        page_incidies = {
            'main_menu': 0,
            'armor_page': 1,
        }
        rect = (1280, 800, 0, 0)
        self.stacked_page_view = StackedPageView(*rect)
        self.stacked_page_view.addPage(MainMenu(*rect, page_incidies))
        self.stacked_page_view.addPage(ArmorPage(*rect, page_incidies))
        self.stacked_page_view.setPage(0)

        self.root.addChild(self.stacked_page_view)