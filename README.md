# Movie App

An awesome web application for browsing and exploring movies. This project demonstrates a simple movie database web app built with Python and Flask, using SQLite for data storage and a clean frontend with custom CSS.

## Table of Contents
- [Features](#features)
- [Architecture](#architecture)
- [Setup Instructions](#setup-instructions)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- List movies with images and details
- Responsive UI with custom CSS
- SQLite database for movie data
- Easy to extend and customize

## Architecture

### Overview
- **Backend:** Python Flask web server
- **Database:** SQLite (`movies.db`)
- **Frontend:** HTML templates (Jinja2), CSS, static images

### Flow Diagram
```
User Request (Browser)
        |
        v
   Flask App (app.py)
        |
        v
   SQLite DB (movies.db)
        |
        v
   HTML Template (index.html)
        |
        v
   Static Files (CSS, Images)
```

### Components
- **app.py:** Main Flask application, handles routing and database queries.
- **create_db.py:** Script to initialize and populate the SQLite database.
- **movies.db:** SQLite database file storing movie information.
- **static/**: Contains CSS and images for the frontend.
- **templates/**: Contains HTML templates rendered by Flask.

## Setup Instructions

1. **Clone the repository**
   ```powershell
   git clone <repo-url>
   cd movie
   ```
2. **Install dependencies**
   ```powershell
   pip install flask
   ```
3. **Initialize the database**
   ```powershell
   python create_db.py
   ```
4. **Run the application**
   ```powershell
   python app.py
   ```
5. **Open in browser**
   Visit `http://127.0.0.1:5000/`

## Project Structure
```
movie/
│   app.py
│   create_db.py
│   movies.db
│   README.md
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── ... (movie images)
│
└── templates/
    └── index.html
```

## Screenshots
> Add screenshots of your app UI here (e.g., homepage, movie details)

## Technologies Used
- Python 3.x
- Flask
- SQLite
- HTML5, CSS3

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
