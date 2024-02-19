# {{ NAME }} Route Design Recipe

## 1. Design the Route Signature

```
# Sort names route
POST /sort-names
  name: string (comma-separated list of names)
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

## 3. Test-drive the Route

```python
"""
 POST /sort-names
  Parameters:
  - names: Eva, David, Edward
  - Expected response (200 OK):

    "David, Edward, Eva"
"""
def test_sort_names(web_client):
    response = web_client.post('/sort_names', data={'names': 'Eva, David, Edward'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "David, Edward, Eva"



"""
POST /sort-names
  Parameters:
  - names: banana, apple, orange
  - Expected response (200 OK):
    "apple, banana, orange"
"""
def test_post_sort_names_alphanumeric(web_client):
    response = web_client.post('/sort-names', data={'names': 'banana, apple, orange'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'apple, banana, orange'


"""
POST /sort-names
  Parameters: none
  - Expected response (200 OK):
  ""
"""
def test_post_sort_names_no_names(web_client):
    response = web_client.post('/sort-names', data={})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''
```
