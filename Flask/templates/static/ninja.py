from jinja2 import Template

name ="Rehnan"

tm = Template("Welcome to the club {{name}}")
msg = tm.render(name=name)
print(msg)