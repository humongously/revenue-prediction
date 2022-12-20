# Flask Backend Example


## SETUP
```cmd
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

# Run Development
```cmd
export ENV=development
flask run
```

# Run production
```cmd
sudo docker-compose build
sudo docker-compose up
```

# Stop production
```cmd
sudo docker-compose down
```