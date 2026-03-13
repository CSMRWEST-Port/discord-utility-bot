FROM python:3.14.3-trixie

RUN pip install discord.py

COPY src/ /src/

CMD ["python", "/src/main.py"]
