MIN_YEAR = 1
MAX_YEAR = 9999


def __check_leap__(day, year):
    if (year % 4) != 0 and day > 28:
        return False
    elif day > 29:
        return False
    return True


def check_date(date):
    day, month, year = (int(item) for item in date.split('.'))
    if not MIN_YEAR < year < MAX_YEAR:
        return False
    elif day <= 0 or month <= 0:
        return False
    match month:
        case 1:
            if day > 31:
                return False
        case 2:
                return __check_leap__(day, year)
        case 3:
            if day > 31:
                return False
        case 4:
            if day > 30:
                return False
        case 5:
            if day > 31:
                return False
        case 6:
            if day > 30:
                return False
        case 7:
            if day > 31:
                return False
        case 8:
            if day > 31:
                return False
        case 9:
            if day > 30:
                return False
        case 10:
            if day > 31:
                return False
        case 11:
            if day > 30:
                return False
        case 12:
            if day > 31:
                return False
        case _:
            return False
    return True


if __name__ == '__main__':
    date = (input('Enter date in format DD.MM.YYYY:\t'))
    print('Date is Ok:\t', check_date(date))
