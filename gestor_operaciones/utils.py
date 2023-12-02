from datetime import datetime, timedelta, time


def dia_semana_actual():
    return datetime.now().date().weekday()

def fecha_actual():
      return str(datetime.now().date())

def adicion_fecha_actual():
    current_date = datetime.now()
    next_month_date = current_date + timedelta(days=30)
    formatted_date = next_month_date.strftime("%Y-%m-%d")
    return str(formatted_date)


def hora_actual():
    return str(datetime.now().time().replace(microsecond=0))

def adicion_hora_actual():
        lst = str(datetime.now().time().replace(microsecond=0)).split(':')
        lst = [int(i) for i in lst]
        h, m, s = lst
        total_time = timedelta(hours=h, minutes=m, seconds=s) + timedelta(hours=6, minutes=0, seconds=0)
        total_seconds = total_time.total_seconds() - total_time.days*86400
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f'{int(hours)}:{int(minutes)}:{int(seconds)}'


def comprobar_hora(h_desde, h_hasta, hora_actual):
    h_actual = datetime.strptime(hora_actual(), '%H:%M:%S').time()

    if h_actual >= h_desde and h_actual <= h_hasta:
         return True
    return False
