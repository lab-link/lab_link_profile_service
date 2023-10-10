# lab-link-profile-service
Flask microservice that handles backend requests for lab link. 

Utilizes SQL Alchemy to persist data through an ORM.
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

### Uncomment this line to seed the database with profile, organization, and project data
```@app.cli.command("seed-db")```
```def seed_db():```
    ```seed_profile_data(db, '../profile_data.json')```
    ```seed_org_data(db, '../org_data.json')```
    ```seed_project_data(db, '../project_data.json')```
    ```print("Database seeded!")```
    
#### How to run seed-db command
```flask seed-db```
