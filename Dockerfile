FROM python:3.14.3-trixie

RUN pip install discord.py psycopg2

COPY src/ /src/

CMD ["python", "/src/main.py"]
