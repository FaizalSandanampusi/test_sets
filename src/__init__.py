"""
Dictionary Template Validator Package
"""

from .dictionary_template import validate
from .dictionary_merge import merge_with_defaultdict, merge_with_counter

__all__ = ['validate', 'merge_with_defaultdict', 'merge_with_counter']

