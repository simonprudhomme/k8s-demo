# python image slim 3.11
FROM python:3.11-slim

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt /app/requirements.txt

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . /app

# command to run on container start, uvicorn server:app --host 0.0.0.0 --port 80
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]
