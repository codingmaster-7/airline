FROM python:3
COPY .  /Desktop/Lecture1/Container
WORKDIR /Desktop/Lecture1/Container
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]