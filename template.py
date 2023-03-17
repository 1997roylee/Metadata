class Template(object):
    def __init__(self, attributes = {}):
        self.attributes = attributes

    def __json__(self):
        return {
            "name": self.attributes["name"],
            "description": self.attributes["description"],
            "symbol": self.attributes["symbol"],
            "image": self.attributes["image"],
            "attributes": self.attributes["attributes"],
            "external_url": "https://travel3.app",
            "properties": {
                "files": [
                    self.attributes.get("file")
                ]
            }
        }