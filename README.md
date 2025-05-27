# EduSwapper

EduSwapper is a platform that connects people who want to teach with those who want to learn. Users can share their expertise, earn tokens, and acquire new skills.

## Features

- **User Authentication**: Register and login securely
- **Profile Management**: Add personal information, education history, work experience, skills to share, and skills to acquire
- **Conference Space**: Join lecture sessions, view your schedule, use interactive whiteboard, and manage assignments
- **Token Leaderboard**: See top users and most popular skills on the platform

## Tech Stack

- **Backend**: Flask, SQLAlchemy, Flask-Login
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Database**: SQLite (file-based, no separate installation needed)

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Setup

1. **Clone or unzip the repository**

```bash
cd eduswapper_fullstack
```

2. **Create a virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Run the application**

```bash
python -m src.main
```

6. **Access the application**

Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
eduswapper_fullstack/
├── venv/                  # Virtual environment
├── src/
│   ├── models/            # Database models
│   │   └── user.py        # User and profile-related models
│   ├── routes/            # Flask routes
│   │   ├── auth.py        # Authentication routes
│   │   └── main.py        # Main application routes
│   ├── static/            # Static files (CSS, JS, images)
│   ├── templates/         # HTML templates
│   │   ├── auth/          # Authentication templates
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   ├── profile.html
│   │   │   └── ...
│   │   ├── base.html      # Base template
│   │   ├── index.html     # Homepage
│   │   ├── conference.html
│   │   └── leaderboard.html
│   ├── forms.py           # Form definitions
│   └── main.py            # Application entry point
└── requirements.txt       # Python dependencies
```

## Usage

1. **Register a new account**
   - Navigate to the registration page
   - Fill in your details and create an account

2. **Complete your profile**
   - Add your education history
   - Add your work experience
   - Specify skills you can teach
   - Specify skills you want to learn

3. **Explore the platform**
   - Browse upcoming lecture sessions
   - Check the leaderboard
   - Join sessions or create your own

## Database

This application uses SQLite, which stores all data in a single file (`eduswapper.db`) that will be created automatically when you first run the application. No additional database setup is required.

## Development

To contribute to the project:

1. Create a new branch for your feature
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
