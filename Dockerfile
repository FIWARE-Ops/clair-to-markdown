FROM python:3.9.5

ENV REPORT_FILE="/github/workspace/report.json"
ENV MARKDOWN_FILE="/github/workspace/report.md"
ENV MUSTACHE_TEMPLATE="./report.md.mustache"

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["/usr/src/app/clair-to-markdown.py"]

ENTRYPOINT ["python3"]