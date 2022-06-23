import inspect
import extruct
import requests
from typing import Optional, Union

from ._utils import *
from ._settings import *
from ._exceptions import *

# Nutrition API


class DefaultSchema:
    def __init__(self, url: str, headers: Optional[dict] = HEADERS):
        """
        url : str
            url
        headers : dict, Optional
            dict
        """
        self.url = url
        self.page = get_html(url)
        self.metadata = scrape(url=url, headers=headers)
        for syntax in SYNTAXES:
            meta = self.metadata.get(syntax, {})
            if len(meta) > 0:
                meta = meta[0]

            else:
                continue

            metatype = meta.get("@type", "")
            graphtype = meta.get("@graph", None)

            if metatype.lower() == "recipe":
                self.data = meta
                return

            elif isinstance(graphtype, list):
                for graph_item in graphtype:
                    if graph_item.get("@type", "").lower() == "recipe":
                        self.data = graph_item
                        return

        self.data = {}

    def title(self) -> str:
        """
        """
        return self.data.get("name", "")

    def author(self) -> str:
        """
        """
        author = self.data.get("author", "")
        if author and isinstance(author, dict):
            return author.get("name", "")

        if (
            author
            and isinstance(author, list)
            and len(author) >= 1
            and isinstance(author[0], dict)
        ):
            return author[0].get("name", "")

        return author

    def time(self) -> float:
        """
        """
        if not (self.data.keys() & {"totalTime", "prepTime", "cookTime"}):
            return float("NaN")

        def _get_key_and_minutes(k):
            return get_minutes(self.data.get(k), return_zero_on_not_found=True)

        time = _get_key_and_minutes("totalTime")
        if not time:
            times = list(map(_get_key_and_minutes, ["prepTime", "cookTime"]))
            time = times(sum)
        # normalize text in utils
        return time

    def yields(self) -> Union[str, list]:
        """
        """
        yields = self.data.get("recipeYield", [])
        return yields

    def instructions(self) -> list:
        """
        """
        instructions = self.data.get("recipeInstructions", "")

        if isinstance(instructions, list):
            text = []
            if isinstance(instructions[0], dict):
                for instruct in instructions:
                    if instruct.get("@type", "").lower() == "howtostep":
                        text.append(instruct.get("text"))

            elif isinstance(instructions[0], str):
                text = instructions

            return text

        else:
            return instructions

    def ratings(self) -> float:
        """
        """
        ratings = self.data.get("aggregateRating", {})
        if len(ratings) == 0:
            return float("NaN")

        if isinstance(ratings, dict):
            ratings = ratings.get("ratingValue")

        if ratings is None:
            return float("NaN")

        return round(float(ratings), 2)

    def reviews(self) -> list:
        """
        """
        return self.data.get("ratings", None)

    def category(self) -> list:
        """
        """
        return self.data.get("recipeCategory", "")

    def cuisine(self) -> str:
        """
        """
        cuisine = self.data.get("recipeCuisine", "")
        if isinstance(cuisine, list):
            return ",".join(cuisine)

        return cuisine

    def nutrition(self, query: bool = True) -> dict:
        """
        """
        nutrition = self.data.get("nutrition", {})

        # Might use api to search this if information if it doesn't exist
        if len(nutrition) == 0 and query:
            return {}

        for key, value in nutrition.copy().items():
            if value is None:
                del nutrition[key]

            elif type(value) in [int, float]:
                nutrition[key] = str(value)

        return nutrition

    def ingredients(self) -> list:
        """
        """
        ingredients = self.data.get("recipeIngredient", [])
        if len(ingredients) > 0:
            return [clean_vulgar_fraction(ingredient) for ingredient in ingredients]

        ingredients = self.data.get("ingredients", [])
        return [clean_vulgar_fraction(ingredient) for ingredient in ingredients]

    def image(self) -> str:
        """
        """
        image = self.data.get("image", "")
        if isinstance(image, dict):
            return image.get("url", "")

        if isinstance(image, list) and len(list) >= 1:
            return image[0]

        return image

    def description(self) -> str:
        """
        """
        return self.data.get("description", "")

    def keywords(self) -> dict:
        """
        """
        return self.data.get("keywords", "")

    def get_all(self) -> dict:
        """
        """
        values = {}
        for method, f in inspect.getmembers(self, predicate=inspect.ismethod):
            if method != "get_all" and not method.startswith("_"):
                values[method] = f()

        return values
