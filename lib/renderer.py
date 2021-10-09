from jinja2 import Template


class TemplateRenderer():
    """Provides an easy interface to the templating engine"""

    def _init_(self, template: str) -> None:
        """Instantiates the engine with the specified template"""
        self.template: Template = Template(open(template, "r").read())

    def render(self,  data: dict) -> str:
        """Renders a template with the given data"""
        return self.template.render(**data)