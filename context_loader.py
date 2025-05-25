import csv
import chardet

class Context:
    def load():
        user_inputs = []
        responses = []
        def detect_encoding(file_path):
            with open(file_path, 'rb') as f:
                result = chardet.detect(f.read())
                return result['encoding']

        encoding = detect_encoding('context.csv')
        with open('context.csv', newline='', encoding=encoding) as csvfile:
            spamreader = csv.reader(csvfile, quotechar='"')
            for row in spamreader:
                for element in row:
                    part1, part2 = element.split(";")
                    user_inputs.append(part1)
                    responses.append(part2)

        return (user_inputs, responses)
    
Context.load()