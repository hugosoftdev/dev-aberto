from babel import dates, numbers
import locale
from datetime import date
from datetime import date, datetime, time
import gettext


if __name__ == '__main__':
    
    gettext.install('cli', localedir='locale')


    today = date.today()
    print(today)
    print(dates.format_date(today))

    number = 240000000000.32212
    print(numbers.format_decimal(number))
    
    name = input(_('Input your name: '))
    print(_('Hello, ') + '{}'.format(name))