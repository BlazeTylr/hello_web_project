"""
POST /sort-names
  Parameters:
  - names: Eva, David, Edward
  - Expected response (200 OK):

    "David, Edward, Eva"
"""
def test_sort_names(web_client):
    response = web_client.post('/sort_names', data={'names': 'Eva,David,Edward'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "David,Edward,Eva"



"""
POST /sort-names
  Parameters:
  - names: banana, apple, orange
  - Expected response (200 OK):
    "apple, banana, orange"
"""
def test_post_sort_fruit_names(web_client):
    response = web_client.post('/sort_names', data={'names': 'banana,apple,orange'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'apple,banana,orange'



"""
POST /sort-names
  Parameters: none
  - Expected response (200 OK):
  ""
"""
def test_post_sort_names_no_names(web_client):
    response = web_client.post('/sort_names', data={'names': ''})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''