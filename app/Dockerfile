FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

RUN api alembic revision --autogenerate -m "First migration"

RUN alembic upgrade head

CMD ["python", "main.py"]
