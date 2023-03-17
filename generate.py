import json
from template import Template
import shutil

NAME = "2022 Iron Game Macau Champions NFT"
DESCRIPTION = "The First Bodybuilding and Strength Competition in Macau, details: https://linktr.ee/theirongame"
SYMBOL = "IG_M_2022"


def generate_image(id):
    return "https://s3.ap-northeast-1.amazonaws.com/travel3.storage/alpha/IG_M_2022/{}.png".format(id)


def generate(id):
    metadata = Template({
        "name": NAME,
        "description": DESCRIPTION,
        "symbol": SYMBOL,
        "image": generate_image(id),
        "attributes": [
            {
                "trait_type": "Background",
                "value": "Throne",
            },
            {
                "trait_type": "Material",
                "value": "Gold",
            },
            {
                "trait_type": "Competition",
                "value": "Iron Game",
            },
            {
                "trait_type": "Glory",
                "value": "Champion",
            }
        ],
        "file": {
            "uri": "{}.png".format(id),
            "type": "image/png"
        }
    })

    with open("./output/{}.json".format(id), 'wb') as file:
        file.write(json.dumps(metadata.__json__()).encode('utf-8'))

    shutil.copyfile("./output/{}.json".format(id), "./output/{}".format(id))
    shutil.copyfile("./origin.webp", "./output/{}.webp".format(id))
    shutil.copyfile("./origin.png", "./output/{}.png".format(id))

if __name__ == "__main__":
    for i in range(35):
        generate(i)
