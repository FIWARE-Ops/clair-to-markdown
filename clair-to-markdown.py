from enum import Enum
from logging import critical
import os
import json
import pystache

class Severity(Enum):
    No = 0
    Negligible = 1
    Low = 2
    Medium = 3
    High = 4
    Critical = 5
    Defcon1 = 6
    # ignore for summary
    Unknown = -1

def get_summary(json_report): 
    count = 0
    neg_count = 0
    low_count = 0
    medium_count = 0
    high_count = 0
    critical_count = 0
    defcon_count = 0
    badge="[Summary](https://img.shields.io/badge/Severity-None-brightgreen)"
    highest = Severity.Negligible

    for vulnerability in json_report["vulnerabilities"]:
        count = count+1
        severity=Severity[vulnerability["severity"]]
        if severity.value > highest.value :
            highest = severity
        if severity is Severity.Negligible:
            neg_count = neg_count+1
        if severity is Severity.Low:
            low_count = low_count+1
        if severity is Severity.Medium:
            medium_count = medium_count+1
        if severity is Severity.High:
            high_count = high_count+1
        if severity is Severity.Critical:
            critical_count = critical_count+1
        if severity is Severity.Defcon1:
            defcon_count = defcon_count+1
    
    if highest is Severity.Negligible:
        badge="![Summary](https://img.shields.io/badge/Severity-Negligible-green)"
    if highest is Severity.Low:
        badge="![Summary](https://img.shields.io/badge/Severity-Low-yellowgreen)"
    if highest is Severity.Medium:
        badge="![Summary](https://img.shields.io/badge/Severity-Medium-yellow)"
    if highest is Severity.High:
        badge="![Summary](https://img.shields.io/badge/Severity-High-orange)"
    if highest is Severity.Critical:
        badge="![Summary](https://img.shields.io/badge/Severity-Critical-red)"
    if highest is Severity.Defcon1:
        badge="![Summary](https://img.shields.io/badge/Severity-Defcon1-blueviolet)"

    
    return {'badge': badge, 'highest': highest.name, 'count': count, 'neg_count' : neg_count, 'low_count': low_count, 'medium_count': medium_count, 'high_count': high_count, 'critical_count': critical_count, 'defcon_count': defcon_count }


report_file = os.getenv("REPORT_FILE")
markdown_file = os.getenv("MARKDOWN_FILE")
mustache_file = os.getenv("MUSTACHE_TEMPLATE")

json_file = open(report_file)
json_report = json.load(json_file)

json_report["summary"] = get_summary(json_report)

mustache_template = open(mustache_file)
template_string = mustache_template.read() 


rendered_report = pystache.render(template_string, json_report)
with open(markdown_file, "w") as markdown_report:
    markdown_report.write(rendered_report)