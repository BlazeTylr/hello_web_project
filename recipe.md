# {{ NAME }} Route Design Recipe

## 1. Design the Route Signature

```
# Sort names route
POST /sort-names
  name: string (comma-separated list of names)
```

```
# Add name route
GET /add_name
  name: string
```

## 2. Create Examples as Tests

```python

# POST /sort-names
#  Parameters:
#  - names: Eva, David, Edward
#  - Expected response (200 OK):
"""
David, Edward, Eva
"""

# POST /sort-names
#  Parameters:
#  - names: banana, apple, orange
#  - Expected response (200 OK):
"""
apple, banana, orange
"""
```

```python

# GET /add_name
#  Parameters:
#  - name: Balazs
#  - Expected response (200 OK):
"""
John, Ben, Balazs
"""

# POST /add_name
#  Parameters:
#  - names: banana
#  - Expected response (200 OK):
"""
John, Ben, banana
"""
```

## 3. Test-drive the Route

```python
"""
POST /sort-names
  Parameters:
  - names: Eva, David, Edward
  - Expected response (200 OK):

    "David,Edward,Eva"
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
```

```python
"""
GET /add_name
  Parameters:
  - name: Balazs
  - Expected response (200 OK):

    "John, Ben, Balazs "
"""
def test_add_name(web_client):
    response = web_client.post('/add_name', data={'name': 'Balazs'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "John, Ben, Balazs"


"""
GET /add_name
  Parameters:
  - name: Balazs
  - Expected response (200 OK):

    "John, Ben, banana"
"""
def test_fruit_name(web_client):
    response = web_client.post('/add_name', data={'name': 'banana'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "John, Ben, banana"

"""
GET /sort-names
  Parameters: none
  - Expected response (200 OK):

    "John, Ben"
"""
def test_add_no_name(web_client):
    response = web_client.post('/add_name', data={'name': ''})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'John, Ben'
```
