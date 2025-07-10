from rich.syntax import Syntax
from urllib.parse import quote_plus
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt

from rich.console import Console
from rich.style import Style
from rich.theme import Theme

white = {
    'highlight': False,
    'style': Style(color="rgb(220,220,220)", italic=False, bold=True),
}

console = Console(theme=Theme({"repr.number": Style(color="bright_yellow", italic=True),}))
pprint = console.print

def print_html(soup):
    if not isinstance(soup, bs):
        soup = bs(str(soup), "html.parser")

    syntax = Syntax(soup.prettify(), "html", theme="monokai", line_numbers=True, word_wrap=True)
    pprint(syntax)