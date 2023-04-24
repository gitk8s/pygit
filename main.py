#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)

# Define the app version
app_version = '1.0'

def code_color(version):
    # Map each version to a corresponding color
    color_map = {
        '1.0': 'Blue',
        '2.0': 'Green'
    }
    # Return the color corresponding to the given version, or "Unknown" if not found
    return color_map.get(version, 'Unknown')

@app.route('/hello/<name>')
def hello(name):
    # Build the greeting message with the user's name and the app version
    greeting = 'Hello {}, we\'re running ver {}.\nCode {}\n'.format(name, app_version, code_color(app_version))
    return greeting

if __name__ == '__main__':
    #app.run(host='example.com', port=80)
    app.run(host='127.0.0.1', port=8080)
