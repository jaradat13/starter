# Starter Django Project

This repository contains a robust Django starter project designed to provide a solid foundation for building modern web applications. It demonstrates best practices for user authentication, profile management, social login integration, and responsive front-end design using Bootstrap and crispy forms.

## Key Features

- **User Authentication & Management**
  - Custom user model with email-based registration.
  - Sign In, Sign Up, and Sign Out functionalities.
  - Profile management with update forms and image uploads.
  - Integrated with [Django Allauth](https://django-allauth.readthedocs.io/) for social authentication (Google OAuth).

- **Responsive Front-End**
  - Uses [Bootstrap 5](https://getbootstrap.com/) for responsive, mobile-first design.
  - Custom CSS for additional styling.
  - Crispy forms integration for elegant form rendering.

- **Static & Informational Pages**
  - Includes essential pages such as Home, About, and Contact.
  - Navbar with dropdown menus for user actions (Profile & Sign Out).

- **Environment & Security**
  - Sensitive configuration (such as `SECRET_KEY` and OAuth credentials) is managed via a `.env` file.
  - The `.env` file and other development artifacts (like `db.sqlite3` and virtual environment directories) are excluded from version control via `.gitignore`.

- **Development Tools & Workflow**
  - SQLite3 is used as the default development database for easy setup.
  - Ready-to-use Git configuration for collaborative development.

## Getting Started

### Prerequisites

- Python 3.8+  
- [pip](https://pip.pypa.io/)  
- [virtualenv](https://virtualenv.pypa.io/)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/jaradat13/starter.git
   cd starter

2. **Create and activate a virtual environment:**
    ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate


3. **Install dependencies:**
    ```bash
   pip install -r requirements.txt

4. **Set up your environment variables:**
Create a .env file in the root of the project and add your settings:

    ```bash
    DJANGO_SECRET_KEY=your-secret-key
    DJANGO_DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    GOOGLE_CLIENT_ID=your-google-client-id
    GOOGLE_CLIENT_SECRET=your-google-client-secret


5. **Apply database migrations:**

    ```bash
    python manage.py migrate

6. **Run the development server:**
    ```bash
   python manage.py runserver

