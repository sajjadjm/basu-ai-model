# pull the official base image
FROM python:3.11

# set work directory
WORKDIR /usr/src/app

# install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# copy project
COPY . .

CMD [ "python", "./server.py" ]
