FROM python:3.12
WORKDIR /task
COPY . .
RUN pip install -r libraries.txt
CMD ["python", "subnet_analyzer.py"]
