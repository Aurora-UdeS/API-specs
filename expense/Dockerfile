FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=expense.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=9001
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 9001
COPY . .
CMD ["flask", "run"]