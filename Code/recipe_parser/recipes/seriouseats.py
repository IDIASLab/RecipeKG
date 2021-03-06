from ._schema import DefaultSchema
from ._utils import get_minutes, get_yields, normalize_string


class SeriousEats(DefaultSchema):
    @classmethod
    def host(cls):
        return "seriouseats.com"

    def author(self):
        author = self.soup.find("meta", {"name": "sailthru.author"})
        return author["content"] if author else None

    def title(self):
        return self.soup.find("h1").get_text()

    def total_time(self):
        return get_minutes(
            self.soup.find("div", {"class": "total-time"}).find(
                "span", {"class": "meta-text__data"}
            )
        )

    def yields(self):
        return get_yields(
            self.soup.find("div", {"class": "recipe-yield"}).find(
                "span", {"class": "meta-text__data"}
            )
        )

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"class": "ingredient"})
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.findAll("li", {"class": "mntl-sc-block-group--LI"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def ratings(self):
        rating = self.soup.find("meta", {"property": "og:rating"})
        rating = (
            round(float(rating["content"]), 2) if rating and rating["content"] else -1.0
        )
        return rating
