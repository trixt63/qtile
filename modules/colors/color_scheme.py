from abc import ABC, abstractmethod


class ColorScheme(ABC):
    @property
    @abstractmethod
    def background(self):
        pass

    @property
    @abstractmethod
    def foreground(self):
        """for other monitor"""
        pass

    # @property
    # @abstractmethod
    # def background_alt(self):
    # """for other monitor"
    #     pass

    # @property
    # @abstractmethod
    # def foreground_alt(self):
    #     pass

    @property
    @abstractmethod
    def background_unfocus(self):
        pass

    @property
    @abstractmethod
    def foreground_unfocus(self):
        pass

    @property
    @abstractmethod
    def background_focus(self):
        pass

    @property
    @abstractmethod
    def foreground_focus(self):
        pass

    @property
    @abstractmethod
    def border_focus(self):
        pass

    @property
    @abstractmethod
    def border(self):
        pass

    @property
    @abstractmethod
    def urgent(self):
        pass