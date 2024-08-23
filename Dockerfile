FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install pipenv
RUN pipenv --python 3.9
RUN pipenv sync
RUN pipenv shell
# Make port 8080 available to the world outside this container
EXPOSE 8080
RUN cd robotframeworker
# Run app.py when the container launches
CMD robot --pythonpath . --debug logs  tests/SAA006.robot