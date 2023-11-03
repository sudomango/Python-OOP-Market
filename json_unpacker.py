import json

class JsonUnpacker:

    def unpack(self, filename: str) -> dict:
        with open(filename, "r", encoding = "UTF-8") as json_file:
            content = json_file.read()
            if content:
                json_dict = json.loads(content)
                return json_dict
            else:
                return {}