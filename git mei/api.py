from typing import Text
import wolframalpha
client = wolframalpha.Client('XEYAPX-APW6G94WL4')

while True:
    query = str(input('chiedi ciò che vuoi: '))
    res = client.query (query)
    output = next(res.results).text
    print(output)