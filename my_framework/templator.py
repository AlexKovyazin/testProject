from jinja2 import Environment, FileSystemLoader


def render(template_name, folder='templates', static_url='/static/', **kwargs):
    """
    :param template_name: имя шаблона
    :param folder: папка, где расположен шаблон
    :param kwargs: параметры, передаваемые в шаблон
    :param static_url: директория расположения статических файлов
    :return:
    """
    env = Environment()
    env.loader = FileSystemLoader(folder)
    env.globals['static'] = static_url
    template = env.get_template(template_name)
    return template.render(**kwargs)
