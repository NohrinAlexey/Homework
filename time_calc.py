duration = int(input('Введите количество секунд: '))

count_year = 31104000
count_month = 2592000
count_week = 604800
count_day = 86400
count_hour = 3600
count_minute = 60
count_second = 1

result = []

years = duration // count_year
duration = duration % count_year
if years != 0:
    result.append(' {} г. '.format(years))
months = duration // count_month
duration = duration % count_month
if 0 != months:
    result.append(' {} мес.'.format(months))
weeks = duration // count_week
duration = duration % count_week
if weeks != 0:
    result.append(' {} нед.'.format(weeks))
days = duration // count_day
duration = duration % count_day
if days != 0:
    result.append(' {} д.'.format(days))
hours = duration // count_hour
duration = duration % count_hour
if hours != 0:
    result.append(' {} ч. '.format(hours))
minutes = duration // count_minute
duration = duration % count_minute
if minutes != 0:
    result.append(' {} мин.'.format(minutes))
seconds = duration
result.append(' {} сек.'.format(seconds))

print("".join(result))
