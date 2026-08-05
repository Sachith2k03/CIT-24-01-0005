FROM python:3.10-slim
RUN pip install flask psycopg2-binary
WORKDIR /app
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]