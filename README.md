# lab-link-profile-service
Flask microservice that handles profile data requests

## Get Started

### Create .env file for following environment variables
```USERNAME=yourusername```
```PASSWORD=yourpassword```
```HOST=hostname(e.x.localhost)```
```DATABASE=lablink```

### Create virtual environment
```python3 -m venv .venv```

### Activate virtual environment
```source .venv/bin/activate```

### Upgrade Environment
```pip install --upgrade pip```

### Install Project Packages
```pip install -r requirements.txt```

### Start Flask Server in Debug Mode
```flask run --debug```

### Uncomment this line in app.py to seed profiles table in database
```with app.app_context():```
    ```db.create_all()```
