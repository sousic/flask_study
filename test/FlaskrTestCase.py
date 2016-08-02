# -*- coding: UTF-8 -*-
import os, flask_study , unittest, tempfile

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, flask_study.app.config['DATABASE'] = tempfile.mkstemp()
        flask_study.app.config['TESTING'] = True
        self.app = flask_study.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flask_study.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        assert '200' in rv.status

    def login(self, username):
        return self.app.post('/sessions/login/', data=dict(username=username), follow_redirects=True)

    def logout(self):
        return self.app.get('/sessions/logout/', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('test')
        # 서비스 성공시 페이지 리다이렉트 처리 되므로 httpStatus 값의 200으로 성공 유무 확인
        assert '200' in rv.status
        rv = self.logout()
        # 서비스 성공시 페이지 리다이렉트 처리 되므로 httpStatus 값의 200으로 성공 유무 확인
        assert '200' in rv.status

if __name__ == '__main__':
    unittest.main()