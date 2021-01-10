FROM python:3
ADD messyant.py /
RUN pip install flask
RUN pip install flask_restful
RUN pip install pypyodbc==1.3.2
EXPOSE 8080
CMD [ "python", "./messyant.py"]
