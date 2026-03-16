FROM python:3.14.3-trixie

RUN pip install discord.py psycopg2

WORKDIR /src

COPY src/ .

CMD ["python", "/src/main.py"]
