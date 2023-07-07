# flaskTest

This Python application, called `flaskTest`, uses Flask, a lightweight web framework for building web applications. It provides a simple interface for routing requests and rendering HTML templates. This particular application includes two routes: one for a home page and one for a login page.

## Prerequisites

Ensure you have the following installed on your machine:

- Python 3.6+
- Flask

## Installation

To install flaskTest, follow these steps:

1. Clone this repository to your machine.

git clone https://github.com/your_username/flaskTest.git


2. Navigate to the project directory.

cd flaskTest


3. Install the required packages.

pip install flask


## Usage

To start the server, run:

python flaskTest.py


Then, open your web browser and navigate to `http://127.0.0.1:5000/` to see the home page. You can navigate to `http://127.0.0.1:5000/login` to see the login page.

## Routes

- `/` - The root/home page. It returns an HTML page (`index.html`).

- `/login` - The login page. It returns another HTML page (`login.html`).

## Features

- **Session management**: This application uses Flask's session object to manage user sessions. The secret key for the session is set to 'super secret key', and the session lifetime is set to 5 minutes.

## Note

The HTML templates `index.html` and `login.html` should be located in a templates folder in the same directory as your Flask application script. 

**Caution**: In a production environment, ensure to replace the 'super secret key' with a strong, secure key, and it's better not to expose it in the code directly. Consider using environment variables or secure secret storage.

## License

This project is open source, under the terms of the [MIT license](https://opensource.org/licenses/MIT).


Then, open your web browser and navigate to `http://127.0.0.1:5000/` to see the home page. You can navigate to `http://127.0.0.1:5000/login` to see the login page.

## Routes

- `/` - The root/home page. It returns an HTML page (`index.html`).

- `/login` - The login page. It returns another HTML page (`login.html`).

## Features

- **Session management**: This application uses Flask's session object to manage user sessions. The secret key for the session is set to 'super secret key', and the session lifetime is set to 5 minutes.

## Note

The HTML templates `index.html` and `login.html` should be located in a templates folder in the same directory as your Flask application script. 

**Caution**: In a production environment, ensure to replace the 'super secret key' with a strong, secure key, and it's better not to expose it in the code directly. Consider using environment variables or secure secret storage.

## License

This project is open source, under the terms of the [MIT license](https://opensource.org/licenses/MIT).
