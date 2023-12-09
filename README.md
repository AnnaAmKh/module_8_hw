# module_8_hw
Home work #8
Вам потрібно реалізувати функцію для виведення списку колег, яких потрібно привітати з днем народження на тижні.

У вас є список словників users, кожен словник у ньому обов'язково має ключі name та birthday. Така структура представляє модель списку користувачів з їх іменами та днями народження. Де name — це рядок з ім'ям користувача, а birthday — це datetime.date об'єкт, в якому записаний день народження.

Наприклад:

{"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()}

Ваше завдання написати функцію get_birthdays_per_week, яка отримує на вхід список users повертає словник користувачів, яких потрібно привітати по днях на наступному тижні.

Формат словника який повертає функція get_birthdays_per_week в нас буде наступним:

{'Monday': ['Bill', 'Jan'], 'Wednesday': ['Kim']}

Ключ словника це дні тижня "Monday", "Tuesday", "Wednesday", "Thursday", "Friday". Значення це списки користувачів з днями народження на тиждень вперед від поточного дня, включаючи поточний день.

ПРИМІТКА
Для прикладу, якщо я запускаю скрипт в середу, то в ключах "Wednesday", "Thursday", "Friday" дні народження цього тижня, а в ключах "Monday", "Tuesday" зберігаються дні народження наступного тижня. В ключі "Monday" завжди дні народження цього тижня які припали на вихідні.

Критерії оцінювання:
Код повинен бути чистим і дотримуватися стандартів PEP 8.
Функція повинна коректно обробляти всі дні тижня.
Функція повинна коректно враховувати вихідні дні і переносити їх на понеділок.
Функція повинна враховувати випадки, коли день народження вже минув у цьому році.
Функція повинна коректно працювати з порожнім списком користувачів.
Функція повинна коректно враховувати ситуації, коли всі дні народження вже минули у цьому році.
Файл з домашнім завданням main.py має імпорт from datetime import date
Для визначення яка сьогодні дата використовується тільки date.today()
Тиждень починається з понеділка
Ви повинні завантажити наступний репозиторій. Виконання домашнього завдання треба зробити в файлі main.py. Змінювати назви файлів та функцій не можна.

Щоб перевірити правильність виконання функції get_birthdays_per_week вам потрібно запустити файл check_homework.py, який перевіряє п'ять основних тестових випадків, для вашої реалізації функції get_birthdays_per_week:

Тест коли усі дні народження користувачів є у майбутньому і не впадають на вихідні.
Тест коли дні народження деяких користувачів випадають на вихідні.
Тест коли деякі дні народження користувачів вже минули у цьому році.
Тест коли у списку немає користувачів.
Тест коли всі дні народження користувачів вже минули у цьому році.
Якщо всі тести домашнього завдання пройдені він вам сповістить це зеленим кольором в консолі.

img

Якщо тести не пройдено, то сповіщення для не пройденого тесту буде червоного кольору в консолі.

img

Після того як ваш код буде проходити всі тести ви здаєте його на перевірку ментору в LMS.
