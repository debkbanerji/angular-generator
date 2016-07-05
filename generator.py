import re


def create_main_directory():
    print ("Creating project directory...")


def camel_case(text):
    components = text.split(' ')
    return components[0].lower() + "".join(x.capitalize() for x in components[1:])


def kebab_case(text):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', camel_case(text))
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()


print ("""This generator will create the base of your
Node.js + Express + Angular 1 project\n""")

print ("""Note: when entering a module name or the project name,
use lowercase words separated by spaces.
Case conversion will take place automatically.""")

project_name = raw_input("\nEnter your project name\n")
print kebab_case(project_name)
print camel_case(project_name)
