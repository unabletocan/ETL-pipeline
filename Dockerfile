# Deriving the python image
FROM python:3.8-slim

# Create a working directory in Docker, makes life easier when running instructions
WORKDIR /app

# Copies all the source code into our directory to the Docker image
COPY . /app

# installs the libraries we will need to execute the code
RUN pip install psycopg2-binary pandas boto3

# Tell Docker the command to run inside the container
CMD ["python", "main.py"]

