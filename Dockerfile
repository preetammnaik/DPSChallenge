FROM python:3.10.5

# switch working directory
WORKDIR /app

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENV FLASK_APP=main.py

CMD ["python","-m","flask", "run", "--host=0.0.0.0"]