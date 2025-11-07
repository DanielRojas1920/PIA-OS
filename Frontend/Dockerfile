FROM python:3.8

# set a directory for the app
WORKDIR /usr/proyecto_final/Frontend

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 8080

# run the command
CMD ["python", "./app.py"]