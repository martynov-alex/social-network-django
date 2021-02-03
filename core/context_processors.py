import datetime as dt


def footer_year(request):
    """ Добавляет переменную с текущим годом. """
    footer_year = dt.datetime.today().year
    return {'footer_year': footer_year}
