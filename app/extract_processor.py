import json


DO_NOT_INCLUDE = (
    "SALDO DO DIA",
    "REND PAGO APLIC AUT MAIS"
)


with open('itau_dictionary.json') as json_file:
    itau_dict: dict = json.load(json_file)


def formatContentToGoogleSheets(content: str, monthShouldBe: int, person: str):
    result = ''
    for line in content.split('\n'):
        line_result = formatLineToGoogleSheets(line.strip(), monthShouldBe, person)
        if line_result != None:
            result = line_result + '\n' + result # append in head (pull)
    return result


def formatLineToGoogleSheets(row: str, monthShoulBe: int, person: str):
    #try:
        row, value = extractDataFromTail(row)
        registration_date, row = extractDataFromHead(row)
        desc = row

        if desc in DO_NOT_INCLUDE:
            return
        
        date = possiblyExtractDateFromDesc(desc)
        
        if date == None:
            day, month, *rest = registration_date.split('/')
        else:
            day, month = date
            desc = desc[:-5]

        if int(month) != monthShoulBe:
            return

        direction = 'Entrada'
        if value.startswith('-'):
            direction = 'Saída'
            value = value.removeprefix('-')

        refined_desc, type = enrichData(desc)

        result = ';'.join([value, direction, type, day, 'Débito', 'Itaú', person, refined_desc, '', desc])
        return result
    #except Exception as e:
    #    print(e)
    #    return "Erro"


def extractDataFromHead(row: str) -> str:
    parts = row.split(sep=' ', maxsplit=1)
    return parts


def extractDataFromTail(row: str) -> tuple:
    parts = row.rsplit(sep=' ', maxsplit=1)
    return parts


def possiblyExtractDateFromDesc(desc: str) -> tuple:
    date = desc[-5:]
    if date[2] != '/':
        return None
    day, month = date.split(sep='/', maxsplit=1)
    if not day.isdigit() or not month.isdigit():
        return None
    return (day, month)


def enrichData(desc: str):
    refined_desc = ""
    type = ""

    item = findKeyLike(itau_dict, desc)

    if item != None:
        if "desc" in item:
            refined_desc = item["desc"]

        if "type" in item:
            type = item["type"]
            
    return (refined_desc, type)


def findKeyLike(dict: dict, desc: str):
    for key in dict.keys():
        if key in desc:
            item = dict[key]
            return item
    return None