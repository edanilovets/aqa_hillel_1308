import requests

base_url = 'http://127.0.0.1:7070'
content = {'cars': ['Audi, VW', 'Toyota']}
updated_content = {'bikes': ['Honda', 'Suzuki']}


class TestContent:

    def test_add_content(self):
        response_data = requests.post(f'{base_url}/content', json=content)
        data = response_data.json()
        assert response_data.status_code == 200, "Content was not created"
        assert response_data.json().get('message') == 'Content created successfully!'

    def test_get_content(self):
        response_get = requests.get(f'{base_url}/content')
        assert response_get.status_code == 200, "Unable to get content"
        server_content = response_get.json().get('content')
        assert content in server_content

    def test_modify_content(self):
        response = requests.put(f'{base_url}/content/0', json=updated_content)
        assert response.status_code == 200, "Unable modify content"
        assert response.json().get('message') == 'Content updated successfully!'

    def test_deleting_content(self):
        response = requests.delete(f'{base_url}/content/0')
        assert response.status_code == 200, "Unable delete content"
        assert response.json().get('message') == 'Content deleted successfully!'