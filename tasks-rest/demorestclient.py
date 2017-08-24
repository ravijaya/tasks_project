import requests


class CustomRestClient(object):
    def get_tasks(self, url):
        response = requests.get(url)
        return response.json(), response.status_code

if __name__ == '__main__':
    client = CustomRestClient()
    url = 'http://127.0.0.1:5000/todo/api/v1.0/tasks'
    print client.get_tasks(url)
