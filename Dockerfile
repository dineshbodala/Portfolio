FROM arwineap/docker-ubuntu-python3.6
COPY . /myapp
WORKDIR /myapp
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD [ "python3","manage.py", "runserver","0.0.0.0:8000"] 
