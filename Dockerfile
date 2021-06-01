# syntax=docker/dockerfile:1

FROM redhat/ubi8-standard

WORKDIR /tito

COPY . .

RUN pip3 install -r requirements.txt

ARG FLASK_ENV="production"

ENV FLASK_ENV="${FLASK_ENV}" \
    FLASK_APP="tito.py" 

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host", "0.0.0.0" ]
