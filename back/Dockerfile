FROM python:3.8-alpine

# copy the requirements file into the image
COPY . /app

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image

# configure the container to run in an executed manner
ENV TZ=Europe/Moscow
ENTRYPOINT [ "python" ]
CMD ["-m", "app" ]