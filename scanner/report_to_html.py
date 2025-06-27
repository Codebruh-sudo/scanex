import json
from jinja2 import Environment, FileSystemLoader

def render_html(summary_path="reports/summary_report.json"):
    with open(summary_path) as f:
        summary_data = json.load(f)

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")
    rendered = template.render(summary=summary_data)

    with open("reports/scan_report.html", "w") as out:
        out.write(rendered)
    print("✅ HTML report saved to reports/scan_report.html")
