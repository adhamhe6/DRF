# Blog API and React App

A web accessible CRUD API built with Django Rest Framework (DRF) for creating, viewing, and deleting blog posts through a RESTful API, and a React application to consume the Django Rest API.

## Features

- View a list of blog posts through the provided REST API.
- View detailed information about a specific blog post.
- Create new blog posts through the API.
- Delete existing blog posts via API endpoints.
- Utilizes Django's testing framework for unit testing models and APIs.
- Utilizes coverage to measure code test coverage.
- Supports Cross-Origin Resource Sharing (CORS) with the help of django-cors-headers.
- Uses React Router DOM for client-side routing.
- Implements UI components from @material-ui/core library.

## Installation and Setup

### Django API

1. Clone the repository:
    ```shell
    git clone https://github.com/adhamhe6/blog-api-react-app.git
    ```

2. Install the required dependencies:
    ```shell
    pip install -r requirements.txt
    ```

3. Apply database migrations:
    ```shell
    python manage.py migrate
    ```

4. Start the Django development server:
    ```shell
    python manage.py runserver
    ```

### React App

1. Change to the React app directory:
    ```shell
    cd blogapi
    ```

2. Install the required dependencies:
    ```shell
    npm install
    ```

3. Start the React development server:
    ```shell
    npm start
    ```

## Usage

- Access the Django API at: [http://127.0.0.1:8000/api/posts](http://127.0.0.1:8000/api/posts/)
- Access the React app at: [http://localhost:3000/](http://localhost:3000/)

## Testing

To run tests and generate coverage reports, use the following commands:
```shell
coverage run --omit='/venv/' manage.py test
coverage html
```

The coverage reports will be available in the `htmlcov/` directory.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
Feel free to further modify and customize the content to suit your project's needs😃.