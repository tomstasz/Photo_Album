from datetime import datetime


def date_cp(request):
    ctx = {
        'date': datetime.now()
    }

    return ctx

