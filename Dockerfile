FROM python:3.12-slim

# RUN apt-get update && apt-get install -y \
#     tesseract-ocr \
#     libmagic1 \
#     poppler-utils \
#     libreoffice \
#     pandoc \
#     && apt-get clean

WORKDIR /app

COPY requirements.txt .

#RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]