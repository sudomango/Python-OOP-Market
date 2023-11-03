import json

# JsonWorker конвертирует JSON-файл в Python-словарь и обратно (записывает словарь в виде JSON-файла).

class JsonWorker:

    def unpack(self, filename: str) -> dict:
        with open(filename, "r", encoding = "UTF-8") as json_file:
            content = json_file.read()
            if content:
                json_dict = json.loads(content)
                return json_dict
            else:
                return {}

    def pack(self, filename: str, subject: dict) -> bool:
        with open(filename, "w", encoding = "UTF-8") as json_file:
            content = json.dumps(subject)
            json_file.write(content)
            return True