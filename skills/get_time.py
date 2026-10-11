import datetime


def get_time():
    maintenant = datetime.datetime.now()
    heure = maintenant.strftime("%Hh%M")
    return f"Il est {heure}."
