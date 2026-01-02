#jinja2
from jinja2 import Template

TEMPLATE = """ Hello {{ name }} !"""

def main():
    template = Template(TEMPLATE)
    print(template.render(name = "Sid"))

main()