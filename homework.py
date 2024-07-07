def send_email(message, recipient, *, sender="university.help@gmail.com"):


    domains = ['.com', '.ru', '.net'] # возможные почтовые домены
    recipients_domain = recipient[recipient.rfind('.'):] # домен получателя
    senders_domain = sender[sender.rfind('.'):] # домен отправителя

    # проверка адреса отправителя и получателя
    if ('@' not in recipient or recipients_domain not in domains) \
            or ('@' not in sender or senders_domain not in domains):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}!')
        return False

    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return False

    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        return True
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        return True


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')