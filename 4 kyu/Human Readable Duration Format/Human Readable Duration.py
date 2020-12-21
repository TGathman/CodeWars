# Python 3.8, 22 March 2020


def format_duration(seconds):

    if seconds == 0:
        return "now"

    year = seconds // 31536000
    day = seconds % 31536000 // 86400
    hour = seconds % 31536000 % 86400 // 3600
    minute = seconds % 31536000 % 86400 % 3600 // 60
    second = seconds % 31536000 % 86400 % 3600 % 60

    join_list = []

    if year > 0:
        join_list.append(str(year) + " year" if year == 1 else str(year) + " years")

    if day > 0:
        join_list.append(str(day) + " day" if day == 1 else str(day) + " days")

    if hour > 0:
        join_list.append(str(hour) + " hour" if hour == 1 else str(hour) + " hours")

    if minute > 0:
        join_list.append(str(minute) + " minute" if minute == 1 else str(minute) + " minutes")

    if second > 0:
        join_list.append(str(second) + " second" if second == 1 else str(second) + " seconds")

    if len(join_list) == 1:
        return join_list[0]

    if len(join_list) == 2:
        return " and ".join(i for i in join_list)

    if len(join_list) > 2:
        return ", ".join(i for i in join_list[:-1]) + " and " + join_list[-1]
