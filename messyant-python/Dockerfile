FROM python:3
ADD messyant.py /
RUN pip install flask
RUN pip install flask_restful
RUN pip install pyodbc
EXPOSE 8080
CMD [ "python", "./messyant.py"]
