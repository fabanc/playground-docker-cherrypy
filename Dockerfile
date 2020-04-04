# Get an official Docker Image
From python:3.6.4-slim-jessie

# Install the dependencies
RUN pip install cherrypy==11.0

# Set the directory structure
WORKDIR /ws
ADD ws.py .
RUN mkdir logs

# Start web service
ENTRYPOINT ["python", "/ws/ws.py"]
CMD ["--logLevel", "INFO"]
