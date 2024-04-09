# Задає базовий (батьківський) образ.
FROM python:3.12 AS base
# Описує метадані. Наприклад, відомості про те, хто створив і підтримує образ.
LABEL maintainer="Denys Filichkin <denys.philichkin@gmail.com>"

ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}
RUN useradd -m -u $UID docker_user
USER docker_user

# initialization porject
WORKDIR /home/docker_user/app
# Встановлює постійні змінні середовища.
ENV PYTHONDONTWRITEBYCODE=1 PYTHONBUFFERED=1

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "src.main"]