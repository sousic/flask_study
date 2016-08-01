# -*- coding: UTF-8 -*-
"""
플래시 메시지 출력 헬퍼 클래스
플래시 메시지 인덱스 번호로 추출
별다른 인덱스값이 없으면 0번으로 고정 보통 1개만 넣기때문에
"""
class flashed_helper:
    app = ''
    def __init__(self, app):
        app.jinja_env.filters['flashed_messages_helper'] = self.flashed_messages_helper
        self.app = app

    def flashed_messages_helper(self, value, index = 0):
        self.app.logger.debug('flashed_message length : %s', len(value))
        if len(value) > 0:
            return value[index]
        return ''