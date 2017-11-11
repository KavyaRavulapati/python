FROM python:3.6.3
ENV PYTHONUNBUFFERED 1

# Change Timezone to GMT+7
ENV TZ=Asia/Bangkok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update \
    && pip install pipenv

WORKDIR /opt/app

COPY Pipfile Pipfile.lock test.py ./

RUN pipenv install --system --deploy

