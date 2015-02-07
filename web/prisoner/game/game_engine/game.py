from .prisoner import Prisoner


class Game(object):
    def __init__(self):
        self.first = True

    def save_prisoner(self, prisoner_to_save):
        assert prisoner_to_save is Prisoner
        if self.first:
            self.first = False
        else:
            pass

    def get_prisoner(self, which):
        pass
