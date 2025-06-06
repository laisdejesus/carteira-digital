FROM python:3.12


WORKDIR /app


COPY requirements.txt /app/requirements.txt


RUN python -m venv /env \
&& /env/bin/pip install --upgrade pip \
&& /env/bin/pip install --no-cache-dir -r /app/requirements.txt


RUN apt-get update && apt-get install -y apt-transport-https ca-certificates curl gnupg && \
curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | apt-key add - && \
echo "deb https://packages.doppler.com/public/cli/deb/debian any-version main" | tee /etc/apt/sources.list.d/doppler-cli.list && \
apt-get update


COPY . /app


ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ENV PYTHONPATH=/app


EXPOSE 8000


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]