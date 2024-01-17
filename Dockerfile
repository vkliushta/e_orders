FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY reqs/requirements.txt .

RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000

CMD ["python", "e_ordes/manage.py", "runserver", "0.0.0.0:8000"]
