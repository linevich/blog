from pelican import signals


def uncss():
    pass


def register():
    signals.finalized.coonect(uncss)
