FROM python:3.10.4
EXPOSE 8000
WORKDIR /app
RUN pip install flask
RUN pip install python-dotenv
RUN pip install flask-smorest
COPY . .
ENV FLASK_APP=src/app.py
CMD ["flask", "run", "--host", "0.0.0.0", "--port=8000"]