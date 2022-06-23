import inspect
from bs4 import BeautifulSoup
from typing import Optional, Union

from ._settings import HEADERS
from ._schema import DefaultSchema
from ._utils import clean_vulgar_fraction, clean_unicode


class AllRecipes(DefaultSchema):
    """
    """

    @classmethod
    def host(cls):
        return "allrecipes.com"

    def __init__(self, url: str, headers: Optional[dict] = HEADERS):
        """
        url : str
            url
        headers : dict, Optional
            dict
        """
        super().__init__(url)
        self.soup = BeautifulSoup(self.page, "html.parser")

    def title(self):
        """
        """
        return self.soup.find("meta", {"property": "og:title"}).get("content")

    def description(self):
        """
        """
        return self.soup.find("meta", {"property": "og:description"}).get("content")

    def instructions(self):
        """
        """
        tags = self.soup.find("ul", {"class": "instructions-section"}).find_all("p")
        return [tag.get_text() for tag in tags]

    def author(self):
        """
        """
        return self.soup.find("span", {"class": "author-name authorName"}).get_text()

    def ratings(self):
        """
        """
        return self.soup.find("meta", {"name": "og:rating"}).get("content")

    def yields(self):
        """
        """
        pass

    def time(self) -> float:
        """
        """
        pass

    def category(self) -> list:
        """
        """
        return [
            self.soup.find("a", {"class": "breadcrumbs__link--last"})
            .find("span")
            .get_text()
        ]

    def nutrition(self) -> dict:
        """
        """
        nutrition = {}
        text = (
            self.soup.find("div", {"class": "recipe-nutrition-section"})
            .find("div", {"class": "section-body"})
            .get_text()
            .strip()
        )
        if text.endswith("Full Nutrition"):
            text = text.replace(". Full Nutrition", "")

        text = text.split(";")
        nutrition["Calories"] = float(text[0].split(" ")[0])

        for t in text[1:]:
            nutrient, amount = t.strip().split(" ")
            nutrition[nutrient] = amount

        return nutrition

    def ingredients(self) -> list:
        """
        """
        tags = self.soup.find_all("span", {"class": "ingredients-item-name"})
        return [clean_unicode(tag.get_text()) for tag in tags]
