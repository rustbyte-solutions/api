FROM python:bullseye

WORKDIR /main
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8888
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]
