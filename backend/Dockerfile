FROM python:3.10-alpine

# change directory
WORKDIR /usr/src/app

# creates virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip

# install python modules needed by the python app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy files required for app to run
COPY app.py .
COPY app .

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD export ENV=production && python -m flask run --host=0.0.0.0