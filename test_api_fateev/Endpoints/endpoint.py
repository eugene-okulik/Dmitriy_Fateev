class EndPoint:
    url = 'http://objapi.course.qa-practice.com'
    headers = {'Content-Type': 'application/json'}
    response = None

    def check_that_status_is_200(self):
        assert self.response.status_code == 200