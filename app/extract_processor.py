def formatContentToGoogleSheets(content: str, monthShouldBe: int, person: str):
    result = ''
    for line in content.split('\n'):
        line_result = formatLineToGoogleSheets(line.strip(), monthShouldBe, person)
        if line_result != None:
            result += line_result + '\n'
    return result


def formatLineToGoogleSheets(row: str, monthShoulBe: int, person: str):
    try:
        row, value = extractDataFromTail(row)
        date, row = extractDataFromHead(row)
        description = row

        if description == 'SALDO DO DIA':
            return
        
        day, month, *rest = date.split('/')

        if int(month) != monthShoulBe:
            return

        direction = 'Entrada'
        if value.startswith('-'):
            direction = 'Saída'
            value = value.removeprefix('-')

        result = ';'.join([value, direction, '', day, 'Débito', 'Itaú', person, '', '', description])
        return result
    except:
        return "Erro"


def extractDataFromHead(row: str) -> str:
    parts = row.split(sep=' ', maxsplit=1)
    return parts


def extractDataFromTail(row: str) -> tuple:
    parts = row.rsplit(sep=' ', maxsplit=1)
    return parts