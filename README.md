# WebProxy

## Overview

WebProxy is a simple web proxy server built using Flask. It allows users to proxy requests to a specified target URL, modifying links in the response content to go through the proxy route. The project includes features like handling 404 errors by redirecting to the last successfully loaded URL with the current path.

## Features

- Proxy HTTP GET and POST requests to a specified target URL.
- Modify links and script sources in the response content to use the proxy route.
- Handle 404 errors by redirecting to the last successfully loaded URL with the current path.

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/noobSrijon/webproxy.git
    cd webproxy
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask app:**

    ```bash
    python app.py
    ```

4. **Access the proxy server:**

    Open your web browser and navigate to [http://localhost:8000](http://localhost:8000).

## How to Use

1. Open the main page and enter the target URL in the provided form.

2. Click the "Surf" button to submit the form.

3. The proxy will forward the request to the target server and modify links in the response content.

4. Navigate through the proxied pages seamlessly.

## Additional Notes

- The proxy server supports both HTTP GET and POST requests.
- In case of a 404 error, the server will redirect to the last successfully loaded URL with the current path.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - A micro web framework for Python.

## Contributors

- [Srijon Kumar](https://github.com/noobSrijon)

## Issues and Feedback

If you encounter any issues or have suggestions, please [open an issue](https://github.com/noobSrijon/webproxy/issues) on GitHub.
