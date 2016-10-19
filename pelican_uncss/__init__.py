from pelican import signals

from .uncss import Uncss


def uncss_plugin(sender):
    uncss = Uncss(sender)
    uncss.perform()


def register():
    signals.finalized.connect(uncss_plugin)
