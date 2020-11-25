FROM python:3.7
WORKDIR /usr/src/api
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5001"]