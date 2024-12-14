# HikeaEase App

The Hikeaease apps is a web base interface to help user explore the mountain in indonesia

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
4. [Configuration](#configuration)
5. [Contributing](#contributing)
6. [Contact](#contact)

---

## Features

- Feature 1: Book The .
- Feature 2: Another feature worth highlighting.
- Feature 3: Additional functionality.

---

## Installation

Follow these steps to install and set up the application:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/shita87/hikeease.git
   cd hikeease
   ```

2. **Set up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   flask run
   ```

---

## Configuration

If the application requires configuration files or environment variables, include instructions:

1. **Environment Variables:**
   - Create a `.env` file in the root directory:
     ```env
     DEBUG=True
     FLASK_APP=run.py
     FLASK_DEBUG=True
     ASSETS_ROOT=/static/assets
     ```
2. **Custom Configurations:**
   Modify `gunicorn-cfg.py` To you most suitable environment.

   bind = '0.0.0.0:5005'
   workers = 1
   accesslog = '-'
   loglevel = 'debug'
   capture_output = True
   enable_stdio_inheritance = True

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit changes:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-branch
   ```
5. Submit a pull request.

---

## Contact

For questions or suggestions, please reach out:

- **Name:** Roshita Setiorini
- **Email:** shita.dicha@gmail.com
- **GitHub:** [Your GitHub Profile](https://github.com/shita87)