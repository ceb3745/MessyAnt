FROM python:3
ADD messyant.py /
RUN pip install flask
RUN pip install flask_restful
RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc-dev \
    unixodbc \
    libpq-dev
RUN pip install pyodbc
EXPOSE 8080
CMD [ "python", "./messyant.py"]
