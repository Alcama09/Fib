FROM python:3

WORKDIR /app

COPY requirements.txt /app/
RUN python -m pip install -r requirements.txt

COPY fib.py /app/


ENTRYPOINT ["python", "fib.py"]

CMD ["--help"]

