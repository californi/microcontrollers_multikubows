FROM python:3.7
WORKDIR /usr/src/api
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5043

COPY . .

CMD ["python", "app.py"]