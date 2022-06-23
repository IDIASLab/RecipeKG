import re
import html
import extruct
import requests
import unicodedata
from w3lib.html import get_base_url

from ._settings import SYNTAXES

IME_REGEX = re.compile(
    r"(\D*(?P<hours>\d+)\s*(hours|hrs|hr|h|óra))?(\D*(?P<minutes>\d+)\s*(minutes|mins|min|m|perc))?",
    re.IGNORECASE,
)

SERVE_REGEX_NUMBER = re.compile(r"(\D*(?P<items>\d+)?\D*)")

SERVE_REGEX_ITEMS = re.compile(
    r"\bsandwiches\b |\btacquitos\b | \bmakes\b | \bcups\b | \bappetizer\b | \bporzioni\b",
    flags=re.I | re.X,
)

SERVE_REGEX_TO = re.compile(r"\d+(\s+to\s+|-)\d+", flags=re.I | re.X)

UNITS = {
    "(tps.|teaspoons)": "teaspoon",
    "(tbps.|tbps|tablespoons)": "tablespoon",
}


def clean_unicode(string):
    """
    """
    cleaned = string.replace(u"\u2009", " ")
    cleaned = clean_vulgar_fraction(cleaned)
    return cleaned.replace("⁄", "/")


def clean_vulgar_fraction(string):
    cleaned = [
        unicodedata.normalize("NFKC", char)
        if unicodedata.name(char).startswith("VULGAR FRACTION")
        else char
        for char in string
    ]
    return "".join(cleaned)


def cleanhtmltags(raw_html):
    """
    """
    cleanr = re.compile("<.*?>")
    cleantext = re.sub(cleanr, "", raw_html)
    return cleantext


def get_minutes(element, return_zero_on_not_found=False):
    if element is None:
        # to be removed
        if return_zero_on_not_found:
            return 0
        raise ElementNotFoundInHtml(element)

    # handle integer in string literal
    try:
        return int(element)
    except Exception:
        pass

    if isinstance(element, str):
        time_text = element
    else:
        time_text = element.get_text()
    if time_text.startswith("P") and "T" in time_text:
        time_text = time_text.split("T", 2)[1]
    if "-" in time_text:
        time_text = time_text.split("-", 2)[
            1
        ]  # sometimes formats are like this: '12-15 minutes'
    if "h" in time_text:
        time_text = time_text.replace("h", "hours") + "minutes"

    matched = TIME_REGEX.search(time_text)

    minutes = int(matched.groupdict().get("minutes") or 0)
    minutes += 60 * int(matched.groupdict().get("hours") or 0)

    return minutes


def get_yields(element):
    """
    """
    if element is None:
        return ""

    if isinstance(element, str):
        serve_text = element
    else:
        serve_text = element.get_text()

    if SERVE_REGEX_TO.search(serve_text):
        serve_text = serve_text.split(SERVE_REGEX_TO.split(serve_text, 2)[1], 2)[1]

    matched = SERVE_REGEX_NUMBER.search(serve_text).groupdict().get("items") or 0
    servings = "{} serving(s)".format(matched)

    if SERVE_REGEX_ITEMS.search(serve_text) is not None:
        # This assumes if object(s), like sandwiches, it is 1 person.
        # Issue: "Makes one 9-inch pie, (realsimple-testcase, gives "9 items")
        servings = "{} item(s)".format(matched)

    return servings


def normalize_string(string):
    """
    """
    unescaped_string = html.unescape(string)
    cleaned_unicode = clean_unicode(unescaped_string)
    cleaned_unicode = cleanhtmltags(cleaned_unicode)
    return re.sub(
        r"\s+",
        " ",
        cleaned_unicode.replace("\xa0", " ")
        .replace("\n", " ")  # &nbsp;
        .replace("\t", " ")
        .strip(),
    )


def get_html(url: str, headers: dict = {}) -> bytes:
    """
    """
    response = requests.get(url, headers=headers)
    return response.text


def get_metadata(html: bytes, url: str, uniform: bool = True) -> dict:
    """
    """
    metadata = extruct.extract(
        html,
        base_url=get_base_url(url),
        syntaxes=SYNTAXES,
        uniform=uniform,
        errors="log",
    )

    if bool(metadata) and isinstance(metadata, list):
        metadata = metadata[0]

    return metadata


def scrape(url: str, headers: dict = {}) -> dict:
    """Parse structured data from a target page."""
    html = get_html(url, headers=headers)
    metadata = get_metadata(html, url)
    return metadata
