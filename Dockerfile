FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements ./requirements

RUN pip install --upgrade pip --no-warn-script-location; pip install wheel
RUN pip install -r requirements/production.txt --user --no-warn-script-location

COPY . .

ENTRYPOINT ["./scripts/entrypoint.sh"]
