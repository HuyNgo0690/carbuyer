FROM python:3.9.15-alpine3.16

RUN addgroup --system admin && adduser --system --group admin

WORKDIR /app

# Install python packages
RUN python -m pip install --upgrade pip

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
ENV PYTHONPATH=/app

RUN chown -R admin:admin $HOME

USER admin

EXPOSE 8000
CMD ["python", "main.py"]