
"""
DESCRIPTION_DICT = {
    "COF APLICACAO CDB": "Cofrinho",
    "COF RESGATE CDB": "Cofrinho",
    "CACAU": "Cacau Show",
    "UNIVERSIDAD": "Bolsa",
    "SHPP": "Shopee",
    "EXTRA": "ExtraBom",
    "CARON": "Carone",
    "IFD": "IFood",
}
"""

def formatLineToGoogleSheets(row: str, monthShoulBe: int, person: str):
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

    print(value, direction, '', day, 'Débito', 'Itaú', person, '', '', description, sep=';')


def extractDataFromHead(row: str) -> str:
    parts = row.split(sep=' ', maxsplit=1)
    return parts


def extractDataFromTail(row: str) -> tuple:
    parts = row.rsplit(sep=' ', maxsplit=1)
    return parts


file = "itau_extrato_nana_01_05_2025.txt"

with open(file, "r", encoding="utf-8") as f:
    linhas = f.readlines()
    for linha in reversed(linhas):
        formatLineToGoogleSheets(linha.strip(), 4, 'Nana')
        