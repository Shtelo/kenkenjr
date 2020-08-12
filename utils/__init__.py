from .singleton_decorator import singleton  # singleton should be imported before literal
from .splitter import wrap_codeblock, split_by_length
from .literal import get_cog, get_path, get_help, get_brief, get_constant, literals, get_check, reload_literals, \
    get_emoji
from .log import Log
from .fresh_data import FreshData
