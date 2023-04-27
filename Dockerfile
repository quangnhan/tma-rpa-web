# Pull base image
FROM python:3.10

# Create a new user
RUN useradd -m django -s /bin/bash
USER django

# Add ~/.local/bin to the PATH environment variable
ENV PATH=/home/django/.local/bin:$PATH

# Stop python from generate *.pyc file
ENV PYTHONONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /tbot-server

# Install dependencies
COPY Pip* ./
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Start server
CMD ["./docker-entrypoint.sh"]
