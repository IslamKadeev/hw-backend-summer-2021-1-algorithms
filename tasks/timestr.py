__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    if seconds >= 60 * 60 * 24:
        day = seconds // (60 * 60 * 24)
        seconds %= 60 * 60 * 24
        hour = seconds // (60 * 60)
        seconds %= 60 * 60
        minute = seconds // 60
        seconds %= 60

        if day < 10:
            day = '0' + str(day) + 'd'
        else:
            day = str(day) + 'd'

        if hour < 10:
            hour = '0' + str(hour) + 'h'
        else:
            hour = str(hour) + 'h'

        if minute < 10:
            minute = '0' + str(minute) + 'm'
        else:
            minute = str(minute) + 'm'

        if seconds < 10:
            seconds = '0' + str(seconds) + 's'
        else:
            seconds = str(seconds) + 's'

        return day + hour + minute + seconds
    elif seconds >= 60 * 60:
        hour = seconds // (60 * 60)
        seconds %= 60 * 60
        minute = seconds // 60
        seconds %= 60

        if hour < 10:
            hour = '0' + str(hour) + 'h'
        else:
            hour = str(hour) + 'h'

        if minute < 10:
            minute = '0' + str(minute) + 'm'
        else:
            minute = str(minute) + 'm'

        if seconds < 10:
            seconds = '0' + str(seconds) + 's'
        else:
            seconds = str(seconds) + 's'

        return hour + minute + seconds
    elif seconds >= 60:
        minute = seconds // 60
        seconds %= 60

        if minute < 10:
            minute = '0' + str(minute) + 'm'
        else:
            minute = str(minute) + 'm'

        if seconds < 10:
            seconds = '0' + str(seconds) + 's'
        else:
            seconds = str(seconds) + 's'

        return minute + seconds
    else:
        if seconds < 10:
            seconds = '0' + str(seconds) + 's'
        else:
            seconds = str(seconds) + 's'
        return seconds
