FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=timesheet.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=9000
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 9000
COPY . .
CMD ["flask", "run"]