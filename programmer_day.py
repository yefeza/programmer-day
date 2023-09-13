from datetime import datetime, date
from datetime import timedelta

def is_programmer_day(today):
    return today==date(today.year,1,1)+timedelta(days=255)

if __name__ == '__main__':
    today = datetime.today()
    if is_programmer_day(today.date()):
        # NOTE: El día internacional del programador se celebra el 256avo día del año (13 de septiembre, excepto en años bisiestos que es el 12 de septiembre)
        print(f'''
            Feliz dia del programador!
              {today.day} / {today.month} /{today.year}



        ''')
    else:
        print("Un café y a programar!")
