# Stubs for django.template.loader (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .exceptions import TemplateDoesNotExist
from typing import Any, Optional

from django.core.handlers.wsgi import WSGIRequest
from django.template.backends.base import BaseEngine
from django.template.backends.django import DjangoTemplates, Template
from typing import Any, List, Optional, Union

def get_template(template_name: str, using: None = ...) -> Template: ...
def select_template(template_name_list: List[str], using: None = ...) -> Template: ...
def render_to_string(
    template_name: Union[str, List[str]],
    context: Any = ...,
    request: Optional[WSGIRequest] = ...,
    using: Optional[str] = ...,
) -> str: ...
def _engine_list(
    using: Optional[str] = ...
) -> Union[List[BaseEngine], List[DjangoTemplates]]: ...