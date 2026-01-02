from jinja2 import Template

data = [{"name" : "Sid", "surname" : "Bagul", "rollno" : "101"},
        {"name" : "Akash", "surname" : "Kumbhar", "rollno" : "102"}, 
        {"name" : "Siddhant", "surname" : "Abhang", "rollno" : "103"}]

def main():
    temp_file = open("datatemp.html.jinja2", "r")
    TEMPLATE = temp_file.read()
    temp_file.close()

    template = Template(TEMPLATE)
    content = template.render(data = data)

    htmldoc = open('display1.html', 'w')
    htmldoc.write(content)
    htmldoc.close()

if __name__ == "__main__":
    main()