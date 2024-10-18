# Django + RestFramework
## How to Run

Follow the steps below to run the project locally:

### Prerequisites

Ensure you have the following installed on your machine:
- **Python** (v3.6 or above): [Download Python](https://www.python.org/downloads/)
- **pip** (Python package manager): Comes with Python installation
- **Docker** (Optional, if you want to run the project using Docker): [Install Docker](https://docs.docker.com/get-docker/)

## Option 1: Running Locally Without Docker
### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/usaidalam469/SMSClassification-Backend.git
    cd your-repository-name
    ```

2. **Create a virtual environment** (optional but recommended):

    Using `venv`:

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Development Server

To start the Django development server, run:

```bash
python manage.py runserver
```
## Option 2: Running Locally With Docker
1. **Clone the repository**:

    ```bash
    git clone https://github.com/usaidalam469/SMSClassification-Backend.git
    cd your-repository-name
    ```

2. **Build the Docker image**:

    Run the following command in the root of your project:

    ```bash
    docker build -t django-app .
    ```

3. **Run the Docker container**:

    Once the image is built, run the container:

    ```bash
    docker run -p 8000:8000 django-app
    ```

This will start the Django application inside a Docker container, and you can access it at `http://localhost:8000`.
