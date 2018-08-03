FROM python

RUN pip install --no-cache-dir flask
COPY . .
ENV FLASK_APP hello.py
EXPOSE 5000
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
