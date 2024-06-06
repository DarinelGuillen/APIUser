from jinja2 import Template

template_str = """
def {{ method_name }}(self, {{ params }}):
    url = '{{ url }}'
    response = requests.{{ http_method }}(url)
    return response.json()
"""

template = Template(template_str)
method_name = "get_users"
params = ""
url = "https://api.example.com/users"
http_method = "get"

code = template.render(method_name=method_name, params=params, url=url, http_method=http_method)
print(code)
