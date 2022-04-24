FROM python:3.10.4-alpine3.15
WORKDIR /flask_test
COPY requirements.txt /flask_test/requirements.txt
RUN pip install -r requirements.txt
COPY . /flask_test/.
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]