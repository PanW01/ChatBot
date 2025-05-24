import csv

class Context:
    def load():
        user_inputs = []
        responses = []
        
        with open('context.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, quotechar='|')
            for row in spamreader:
                for element in row:
                    part1, part2 = element.split(";")
                    user_inputs.append(part1)
                    responses.append(part2)

        return (user_inputs, responses)