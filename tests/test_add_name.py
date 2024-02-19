"""
GET /add_name
  Parameters:
  - name: Balazs
  - Expected response (200 OK):

    "John, Ben, Balazs "
"""
def test_add_name(web_client):
    response = web_client.get('/add_name?name=Balazs')
    
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "John, Ben, Balazs"


"""
GET /add_name
  Parameters:
  - name: Balazs
  - Expected response (200 OK):

    "John, Ben, banana"
"""
def test_add_fruit_name(web_client):
    response = web_client.get('/add_name?name=banana')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "John, Ben, banana"

"""
GET /sort-names
  Parameters: none
  - Expected response (200 OK):
  
    "John, Ben"
"""
def test_add_no_name(web_client):
    response = web_client.get('/add_name?name=')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'John, Ben'