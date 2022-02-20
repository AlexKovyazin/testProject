from os.path import join
from jinja2 import Template


def render(template_name, folder='templates', **kwargs):
    """
    :param template_name: имя шаблона
    :param folder: папка, где расположен шаблон
    :param kwargs: параметры, передаваемые в шаблон
    :return:
    """
    file_path = join(folder, template_name)

    with open(file_path, encoding='utf-8') as file:
        template = Template(file.read())
        return template.render(**kwargs)
