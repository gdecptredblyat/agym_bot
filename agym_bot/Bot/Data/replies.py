start="Здравствуйте, введите свои фамилию, имя, класс"
add_event="Введите текст события"
add_hw="Введите предмет, дату сдачи, текст задания"
delete_me="ня. пока"
number="Введите фамилию и имя необходимого человека"
next_duty="Вы дежурите"
change_info="Информация сохранена"
not_found="Не найден(а)"
def duty(date):
	return "Вы дежурите {date}".format(date=date)
def mobile(last_name, first_name, number):
	return "Номер телефона ученика {last_name} {first_name}: {number}".format(last_name=last_name, first_name=first_name, number=number)
def hw(subject, date, homework):
	return "Домашнее задание по {subject} на {date}: {homework}".format(subject=subject, date=date, homework=homework)