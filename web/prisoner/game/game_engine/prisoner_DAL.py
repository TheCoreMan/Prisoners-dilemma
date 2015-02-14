from ..models import Prisoner


def save_prisoner(prisoner_to_save):
    assert type(prisoner_to_save) == Prisoner
    prisoner_to_save.save()


def get_prisoner(which):
    if type(which) == str:
        return Prisoner.objects.get(name=which)
    elif type(which) == int:
        return Prisoner.objects.all()[which]


def delete_players_from_db():
    Prisoner.objects.all().delete()
