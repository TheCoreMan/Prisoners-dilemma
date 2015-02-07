from django.db import models


# Create your models here.
class Prisoner(models.Model):
    name = models.CharField(max_length=40, blank=False, help_text="This is the prisoner's name. Enter your name :)")
    strategy = models.CharField(max_length=1500, blank=False, help_text="This is the prisoner's strategy. Write it in Python.")
    years = models.IntegerField(default=0)

    def __str__(self):
        return '\nname: {}\nstrategy: {}\nyears: {!r}'.format(self.name, self.strategy, self.years)