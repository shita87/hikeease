FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /hikeease
WORKDIR /hikeease

COPY requirements.txt .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run Gunicorn with your Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "run:app"]