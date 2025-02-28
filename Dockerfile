FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r high_scores.txt

CMD ["python", "main.py"]
