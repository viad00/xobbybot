# coding=UTF-8
from bot_session import unblock_user, test_get_answer_value, test_get_current_test_score, test_set_question_score, test_get_question, test_del, test_get_max_score


def handler(user_id, answer):
    test_id, score = test_get_current_test_score(user_id)
    ans, value = test_get_answer_value(test_id)
    msg = u''
    test_id += 1
    try:
        if int(answer) == ans:
            test_set_question_score(user_id, test_id, score+value)
            msg += u'Правильно! +{0} Очко\n'.format(value)
        else:
            test_set_question_score(user_id, test_id, score)
            msg += u'Неверно :(\n'
    except Exception:
        msg += u'Укажите правильный номер ответа (одна цифра)\n'
    text, attach = test_get_question(test_id)
    if text != u'NOMORE':
        msg += text
    else:
        test_id, score = test_get_current_test_score(user_id)
        test_del(user_id)
        unblock_user(user_id)
        msg = u'Тест завершён!\nВаш результат: {0} из {1} баллов'.format(score, test_get_max_score())
    return msg, attach
