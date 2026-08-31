FROM python:3.13-slim

WORKDIR /work

# PIP_EXTRA_OPTS is for TLS-intercepting corporate proxies only
# (e.g. --trusted-host pypi.org --trusted-host files.pythonhosted.org).
# Leave empty on normal networks.
ARG PIP_EXTRA_OPTS=""

COPY requirements.txt .
RUN pip install --no-cache-dir ${PIP_EXTRA_OPTS} -r requirements.txt

COPY . .

CMD ["bash"]
