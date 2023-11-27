from datetime import datetime, timedelta, time


def dia_semana_actual():
    return datetime.now().date().weekday()

def fecha_actual():
      return str(datetime.now().date())

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
    elif h_desde > h_hasta:
        x = datetime.strptime('23:59:59', '%H:%M:%S').time()
        y = datetime.strptime('00:00:00', '%H:%M:%S').time()
        if (h_actual >= h_desde and h_actual <= x) or (h_actual >= y and h_actual <= h_hasta):
             return True
    return False

def f(h1, h2, ha):
    h_actual = datetime.strptime(ha(), '%H:%M:%S').time()
     
    if h_actual >= h1 and h_actual <= h2:
         return True
    elif h1 > h2:
        x = datetime.strptime('23:59:59', '%H:%M:%S').time()
        y = datetime.strptime('00:00:00', '%H:%M:%S').time()
        if (h_actual >= h1 and h_actual <= x) or (h_actual >= y and h_actual <= h2):
             return True
    return False