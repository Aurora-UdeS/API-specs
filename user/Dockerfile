FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=user.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=9002
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 9002
COPY . .
CMD ["flask", "run"]