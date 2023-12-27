import random
import json

subject = ['математика', 'англиский', 'физика', 'техника мышления', 'история', 'физра']
room = ['1', '2', '3', '4', '5', '6',
        '7', '8', '9', '10', '11']
group = ['61601', '61602', '63201', '63801', '63401', '63402',
         '63601', '63602', '64201', '64202']
subjects_dict = {
    'математика': ['Горохова Наталья Владимировна', 'Лапин Александр Васильевич', 'Симаков Сергей Сергеевич'],
    'англиский': ['Дьячкова Ирина Евгеньева', 'Антонова Ирина Сергеевна', 'Махмутова Адиля Рифатовна'],
    'физика': ['Садовников Арсений Вадимович', 'Касимов Аслан Рамазанович', 'Девятьяров Кирилл Алексеевич'],
    'техника мышления': ['Гаврилов Максим Викторович', 'Звонова Екатерина Евгеньевна'],
    'история': ['Шматова Маргарита Борисовна'],
    'физра': ['Батракова Светлана Петровна', 'Безуглов Алексей Иванович', 'Деревяшкина Светлана Стенанова',
              'Шелехова Светлана Сергеевна'],
    }
time_start = ['08:15', '09:05', '10:45', '11:35', '12:25', '13:15', '14:05', '14:55', '15:45', '16:35']
time_end = ['11:30', '12:20', '13:10', '14:00', '15:40', '14:50', '15:40', '18:10', '18:10', '18:10']
date = ['09.01.2024']
dump = []
big_dict = {}
index_start_end = []


def choose_subject():
    while True:
        random_subject = subject[random.randint(0, 5)]
        if len(subjects_dict[random_subject]) == 4:
            random_teacher = subjects_dict[random_subject][random.randint(0, 3)]
        elif len(subjects_dict[random_subject]) == 3:
            random_teacher = subjects_dict[random_subject][random.randint(0, 2)]
        elif len(subjects_dict[random_subject]) == 2:
            random_teacher = subjects_dict[random_subject][random.randint(0, 1)]
        else:
            random_teacher = subjects_dict[random_subject][0]
        sub_teach = random_subject + random_teacher
        if sub_teach not in dump:
            dump.append(sub_teach)
            return random_subject, random_teacher


def choose_group():
    while True:
        random_group = group[random.randint(0, 9)]
        if random_group not in dump:
            dump.append(random_group)
            return random_group


def choose_time(index_end_last_lesson):
    for i in range(9):
        if time_start[i] > time_end[index_end_last_lesson]:
            return i


for i in range(9):
    random_time = random.randint(0, 2)
    index_start_end.append(random_time)
    now_subject, now_teacher = choose_subject()
    now_group = choose_group()
    if room[i] in big_dict.keys():
        big_dict[room[i]][date[0]].append((time_start[random_time], time_end[random_time], now_subject, now_teacher, now_group))
    else:
        big_dict[room[i]] = ({date[0]: [(time_start[random_time], time_end[random_time], now_subject, now_teacher, now_group)]})
dump = []

for _ in range(3):
    for j in range(9):
        if time_start[index_start_end[j]] not in ('14:55', '15:45', '16:35'):
            index_start_end[j] = choose_time(index_start_end[j])
            now_time_start = time_start[index_start_end[j]]
            now_time_end = time_end[index_start_end[j]]
            now_subject, now_teacher = choose_subject()
            now_group = choose_group()
            if room[j] in big_dict.keys():
                big_dict[room[j]][date[0]].append((now_time_start, now_time_end, now_subject, now_teacher, now_group))
            else:
                big_dict[room[j]] = {date[0]: [(now_time_start, now_time_end, now_subject, now_teacher, now_group)]}

    dump = []

with open('schedule.json', 'w+', encoding='utf-8') as f:
    json.dump(big_dict, fp=f, ensure_ascii=False)
