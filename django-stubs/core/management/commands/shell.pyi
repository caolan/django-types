from typing import Any, List

from django.core.management import BaseCommand as BaseCommand
from django.core.management import CommandError as CommandError
from django.utils.datastructures import OrderedSet as OrderedSet

class Command(BaseCommand):
    shells: List[str] = ...
    def ipython(self, options: Any) -> None: ...
    def bpython(self, options: Any) -> None: ...
    def python(self, options: Any) -> None: ...