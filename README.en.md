<div align="right">
    <a href="./README.md">🇧🇷 Read in Portuguese</a>
</div>

<div align="center">
    <img src="./static/img/readme-images/icon.png" alt="Portfolio Icon" width="128"/>
</div>

<p align="center">
    A dynamic and modern portfolio website, developed with Python and Flask, showcasing projects, education, and contact information in an interactive way.
</p>

---

## About This Project

This is a single-page application personal portfolio website. The goal is to present a developer's skills, projects, and journey in a professional and visually appealing manner.

All site content, such as personal information, social media links, projects, and education, is centrally managed through a single Python configuration file (`config.py`), making updates simple and fast without needing to alter the HTML code.

### Video Demo

Watch a full demonstration of the live website:

<p align="center">
  <a href="https://youtu.be/AwQg6tu3Gfo" target="_blank">
    <img src="./static/img/readme-images/thumbnail.png" alt="Portfolio Video Demo" width="80%">
  </a>
  <br>
  <em>Click the image to watch the video</em>
</p>

---

### Key Technologies and Concepts

-   **Backend (Python + Flask):** Used to serve the web application and process email submissions from the contact form.
-   **Frontend (HTML, CSS, JavaScript):**
    -   **HTML with Jinja2:** Allows for dynamic content rendering from the backend.
    -   **Modern CSS3:** Animations, responsive layout with Flexbox, and CSS variables for a consistent design. Includes visual effects like animated gradients and smooth transitions.
    -   **JavaScript (Vanilla):** Used for interactivity, such as animations triggered on scroll (`IntersectionObserver`).
-   **Flask-Mail:** A library that integrates SMTP email sending, used to make the contact form functional.
-   **Centralized Content Architecture:** The `config.py` file acts as a single source of truth for all site text and data, facilitating maintenance and customization.
-   **Security:** The `secrets_email.py` file (ignored by Git) is used to store sensitive email credentials, separating them from the main source code.

---

### Main Features

-   **Dynamic Content:** All sections (projects, education, etc.) are generated from the `config.py` file.
-   **Scroll Animations:** Elements smoothly appear on the screen as the user scrolls.
-   **Interactive Home Section:** Displays developer info, social media links, and a technology bar.
-   **Detailed Project Cards:** Each project can display a description, technologies used, an image gallery, and links to "DEMO" and "REPOSITORY".
-   **Functional Contact Form:** Sends an email directly to the portfolio owner through a secure backend.

---

### Screenshots

<p align="center">
  <img src="./static/img/readme-images/home.png" alt="Home Section" width="80%">
  <br>
  <em>Initial presentation section.</em>
</p>

<p align="center">
  <img src="./static/img/readme-images/projects.png" alt="Projects Section" width="80%">
  <br>
  <em>Projects section with detailed cards.</em>
</p>

---

## How to Run the Source Code

To run this project locally, follow the steps below.

### Prerequisites

-   Python 3.x installed on your system.
-   `pip` (Python package manager).

### Installation and Execution

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/NONATO-03/portfolio.git
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd my-portfolio
    ```

3.  **Create and activate a virtual environment (recommended):**
    ```sh
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

5.  **Configure environment variables for email:**
    Create a file named `secrets_email.py` in the project root and fill it with your information, following the template below.

    **Important:** If you use Gmail, you need to generate an **"App Password"** instead of using your regular password. [Go to your Google Account settings](https://myaccount.google.com/apppasswords) to create one.

    ```python
    # secrets_email.py

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'your-email@gmail.com'
    MAIL_PASSWORD = 'your_google_app_password'
    MAIL_RECIPIENT = 'email-where-messages-will-be-sent@example.com'
    ```

6.  **Run the application:**
    ```sh
    python app.py
    ```
    Open your browser and go to `http://127.0.0.1:5000` to see the site.

---

### Author

Developed with ❤️ by **Vitor Nonato Nascimento**.

-   **GitHub:** [https://github.com/NONATO-03](https://github.com/NONATO-03)