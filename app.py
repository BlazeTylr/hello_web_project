import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"


@app.route('/submit', methods=['POST'])
def post_submit():
    name = request.form['name']
    message = request.form['message']
    # DOES NOT RUN: The HTTP method (GET) doesn't match the route's (POST)
    return f'Thanks {name}, you sent this message: "{message}"'
# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.

@app.route('/wave', methods=['GET'])
def get_wave():
    name = request.args['name']
    
    return f'I am waving at {name}'

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']

    vowels = 'aeiou'
    count = 0

    for char in text:
        if char in vowels:
            count += 1            

    return f'There are {count} vowels in "{text}"'

@app.route('/sort_names', methods=['POST'])
def sort_names():
    names = request.form['names']
    names = names.split(',')

    sorted_names = sorted(names)

    return ','.join(sorted_names)

@app.route('/add_name', methods=['GET'])
def add_name():
    base_names = 'John, Ben'
    name = request.args['name']
    if name == '':
        return base_names
    base_names += f", {name}"
    return base_names


from example_routes import apply_example_routes
apply_example_routes(app)



# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

