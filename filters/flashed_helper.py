# -*- coding: UTF-8 -*-
#플래시 메시지 인덱스 번호로 추출
#별다른 인덱스값이 없으면 0번으로 고정 보통 1개만 넣기때문에
def __init__(app):
    app.jinja_env.filters['flashed_messages_helper'] = flashed_messages_helper

def flashed_messages_helper(value, index = 0):
    if len(value) > 0:
        return value[index]
    return ''