FROM python:3.8.10-alpine

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt && rm -rf /requirements.txt

RUN addgroup -g 998 rhasspy-app \
    && adduser rhasspy-app -u 998 --disabled-password --no-create-home --ingroup rhasspy-app \
    && chown -R rhasspy-app /app
USER rhasspy-app

COPY weather_app.py /app 

CMD [ "python3","/app/weather_app.py" ]
