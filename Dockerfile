# Python image.
FROM python:3.8-alpine

# Copy requirements file into image
COPY ./requirements.txt /app/requirements.txt

# Working directory in the container
WORKDIR /app

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the contents into the container
COPY . /app

# Configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["view.py" ]