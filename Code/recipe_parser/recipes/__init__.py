from urllib.parse import urlparse

from ._schema import DefaultSchema
from ._utils import get_metadata, clean_unicode

from .seriouseats import SeriousEats
from .allrecipes import AllRecipes

parsers = {
    SeriousEats.host(): SeriousEats,
    AllRecipes.host(): AllRecipes,
}


def scrape_page(url):
    parsed = urlparse(url)
    parser = parsers.get(parsed.netloc.replace("www.", ""), DefaultSchema)
    return parser(url).get_all()
