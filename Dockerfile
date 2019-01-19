FROM python

RUN apt-get update -qq && apt-get install -y --no-install-recommends && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/app

ENV SECRET_KEY te0!d#h7d72guawd-t$1wu4!!uzb2iy)vw4i8w6f66=)thg$3&
ENV SKT_API_KEY e545a89a-eeda-4769-aade-8afad754bece
ENV DATABASE_NAME schedule_prod
ENV DATABASE_USER root
ENV DATABASE_PASSWORD whgusdnr12
ENV DATABASE_HOST playgillround.cwadawgcd2ch.ap-northeast-2.rds.amazonaws.com

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py migrate --settings=mysite.settings.prod
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "--settings=mysite.settings.prod", "0.0.0.0:8000"]