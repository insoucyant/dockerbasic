# Docker Basic

This repository contains a simple example of using Docker to containerize a Python "Hello, World!" application using Flask. It's designed to help beginners understand the basics of Docker.

## Contents

The repository includes the following files:

* `app.py`: A basic Flask application that returns "Hello, World!".
* `Dockerfile`: A Dockerfile that defines how to build a Docker image for the Flask application.
* `requirements.txt`: A list of Python dependencies (Flask) required for the application.
* `docker-compose.yml`: (Potentially, if you add one later) A Docker Compose file for defining and running multi-container Docker applications.  *(Not present in the original file list, but good to mention)*
* `README.md`: This file.

## Prerequisites

Before you begin, make sure you have the following installed:

* [Docker](https://docs.docker.com/get-docker/)

## Getting Started

Here's how to get the application running using Docker:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/insoucyant/dockerbasic.git](https://github.com/insoucyant/dockerbasic.git)
    cd dockerbasic
    ```

2.  **Build the Docker image:**

    ```bash
    docker build -t my-flask-app .
    ```

    This command builds a Docker image named `my-flask-app` using the instructions in the `Dockerfile`. The `.` specifies that the build context is the current directory.

3.  **Run the Docker container:**

    ```bash
    docker run -p 5000:5000 my-flask-app
    ```

    This command runs a container from the `my-flask-app` image. The `-p 5000:5000` option maps port 5000 on your host machine to port 5000 inside the container, where the Flask application is running.

4.  **View the application:**

    Open your web browser and go to `http://localhost:5000`. You should see the "Hello, World!" message.

## Understanding the Files

### `app.py`

This is a simple Flask application:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
It imports the Flask class.It creates a Flask application instance.It defines a route / that returns the string "Hello, World!".The `if name == "main":
