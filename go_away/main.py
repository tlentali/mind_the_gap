# -*- coding: utf-8 -*-

"""
    main
"""
import argparse
import logging
import time
from pathlib import Path

import pygame
import schedule

import config
from tbm import TbmParser

L = logging.getLogger(__name__)
L.setLevel(logging.DEBUG)
L.addHandler(logging.StreamHandler())


class Resource:
    """
    Resources manager. Load all in memory (the 64k time is over)
    """
    instance = None

    def __init__(self):
        resources_path = Path.joinpath(Path.cwd(), 'resources')
        self.font64 = pygame.font.Font(str(resources_path / "fonts" / "VT323.ttf"), 64)
        self.tramway_sign = pygame.image.load(str(Path.joinpath(resources_path, 'tram.png')))

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Resource()
        return cls.instance


class Label:
    """
    Base class for all text displayed on screen
    """
    def __init__(self, screen, color, text):
        """
        Constructor render a text.

        :param screen: The screen surface to draw on
        :type screen: pygame.surface.Surface
        :param color: The RGB text color
        :type color: tuple
        :param text: The text to display
        :type text: str
        """
        self.screen = screen
        self.rendered = self._render_font(color, text)
        self.position = (0, 0)

    def display_at(self, position):
        """
        Display the text at the given coordinate.

        :param position: The position of the text
        :type position: tuple
        """
        self.screen.blit(self.rendered, position)

    def draw(self):
        """
        Display the text at the position (default is 0,0)
        """
        self.screen.blit(self.rendered, self.position)

    def _render_font(self, color, text):
        """
        Render a font in a certain color and with the text

        :param color:
        :param text:
        :return:
        """
        font = Resource.get_instance().font64
        return font.render(text, True, color)

    def get_width(self):
        """
        Get the rendered font width
        """
        return self.rendered.get_width()

    def get_height(self):
        """
        Get the rendered font height
        """
        return self.rendered.get_height()

    def set_position(self, position):
        """
        Set the position

        :param position: the position
        :type position: tuple
        """
        self.position = position


class TramIcon:
    """
    Display the splash screen
    """
    def __init__(self, screen):
        self.screen = screen

        self.icon = Resource.get_instance().tramway_sign
        self.icon_pos = (screen.get_width() - self.icon.get_width()) // 2, \
                        (screen.get_height() - self.icon.get_height()) // 2 - config.LABEL_MARGIN

        self.label = Label(screen, config.RED, "Chargement")
        self.font_pos = (screen.get_width() - self.label.get_width()) // 2, \
                        self.icon.get_height() + self.icon_pos[1] + config.LABEL_MARGIN

    def draw(self):
        """
        Render into PyGame
        """
        self.screen.blit(self.icon, self.icon_pos)
        self.label.display_at(self.font_pos)


class GoAway:
    """
    Main class.
    """

    def __init__(self, fullscreen):
        """
        Constructor Initialize PyGame
        """
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((1024, 600), pygame.FULLSCREEN if fullscreen else 0)
        self.info = None
        self.tram = TramIcon(self.screen)

    def run(self):
        """
        Main loop. Get and treat events then display.
        """
        L.info('Lets go!')
        quit = False

        schedule.every(config.REFRESH).seconds.do(self.get_tramway_schedule)

        while not quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True

                elif event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                    quit = True

            self.screen.fill(config.BLACK)

            if self.info is None:
                self.tram.draw()

            else:
                for label in self.labels:
                    label.draw()

            pygame.display.flip()
            schedule.run_pending()
            time.sleep(0.1)

    def get_tramway_schedule(self):
        """
        Load TBM schedule from page
        """
        L.info('Loading TBM page')
        parser = TbmParser(config.URL)
        parser.parse()
        self.info = parser.info
        self._create_tramway_labels()

    def _create_tramway_labels(self):
        """
        TBM results are always multiple.
        """
        self.labels = []

        top = config.LABEL_TOP
        for info in self.info:
            label = Label(self.screen, config.RED, "{minutes:2d} minutes {direction}".format(minutes=info.duration,
                                                                                      direction=info.direction))
            label.set_position((config.LABEL_LEFT, top))
            self.labels.append(label)
            top += label.get_height() + config.LABEL_MARGIN


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fullscreen', action="store_true", default=False)
    arg = parser.parse_args()

    GoAway(arg.fullscreen).run()

if __name__ == '__main__':
    main()
