
import os
import json
import pystache

report_file = os.getenv("REPORT_FILE")
markdown_file = os.getenv("MARKDOWN_FILE")
mustache_file = os.getenv("MUSTACHE_TEMPLATE")

json_file=open(report_file)
json_report = json.load(json_file)

mustache_template=open(mustache_file)
template_string= mustache_template.read() 


rendered_report=pystache.render(template_string, json_report)
with open(markdown_file, "w") as markdown_report:
    markdown_report.write(rendered_report)