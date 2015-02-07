from ..models import Prisoner


class Game(object):
    def save_prisoner(self, prisoner_to_save):
        assert type(prisoner_to_save) == Prisoner
        prisoner_to_save.save()

    def get_prisoner(self, which):
        if type(which) == str:
            return Prisoner.objects.get(name=which)
        elif type(which) == int:
            return Prisoner.objects.all()[which]

    def end(self):
        Prisoner.objects.all().delete()
