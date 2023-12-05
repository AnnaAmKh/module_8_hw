from datetime import date, datetime, timedelta

WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
#today  05.12.2023
users_list = [
    {"name": "Bill", "birthday": datetime(year=2023, month=12, day=29).date()},
    {"name": "Andrew", "birthday": datetime(year=2023, month=12, day=2).date()},
    {"name": "Jill", "birthday": datetime(year=2023, month=12, day=9).date()},
    {"name": "Till", "birthday": datetime(year=2023, month=12, day=5).date()},
    {"name": "Jan", "birthday": datetime(year=2023, month=12, day=6).date()},
]


def close_birthday_users(users, start, end):
    now = date.today()
    result = []
    for user in users:
        birthday = user.get('birthday').replace(year=now.year)
        if birthday < now:
            birthday = birthday.replace(year=now.year + 1)
        if now <= birthday <= end:
            result.append(user)
    return result
def get_birthdays_per_week(users):
    now = date.today()
    current_week_day = now.weekday()
    if not users:
        return {}
    start_date = now
    end_date = now + timedelta(days=7)
    birthday_users = close_birthday_users(users, start=start_date, end=end_date)
    result_dict = {}
    for user in birthday_users:
        user_birthday = user.get('birthday').replace(year=now.year)
        if user_birthday < now:
            user_birthday = user_birthday.replace(year=now.year + 1)
        user_birthday_weekday = user_birthday.weekday()
        try:
            user_happy_day = WEEKDAYS[user_birthday_weekday]
        except IndexError:
            user_happy_day = WEEKDAYS[0]
        if user_happy_day not in result_dict:
            result_dict[user_happy_day] = []
        result_dict[user_happy_day].append(user.get('name'))
    return result_dict

if __name__ == "__main__":
    result = get_birthdays_per_week(users_list)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
