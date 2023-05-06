FROM python:3.10-slim

WORKDIR /usr/src

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && \
  apt-get update && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
  pipenv install --deploy --system && \
  apt-get remove -y gcc python3-dev libssl-dev && \
  apt-get autoremove -y && \
  pip uninstall pipenv -y

RUN sed -i 's/method_whitelist/allowed_methods/g' /usr/local/lib/python3.10/site-packages/instagrapi/mixins/public.py
RUN sed -i 's/method_whitelist/allowed_methods/g' /usr/local/lib/python3.10/site-packages/instagrapi/mixins/private.py


COPY . .

CMD ["python", "./app/run.py"]
