import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Escopos necessários para acessar o Google Sheets e Drive
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Caminho para o seu arquivo de chave (baixado do Google Cloud Console)
creds = ServiceAccountCredentials.from_json_keyfile_name("credenciais.json", scope)
client = gspread.authorize(creds)



# Abrir a planilha pelo nome
spreadsheet = client.open_by_key("1uDPh0-PztYsJMQMP00fPBPgu0YwRx2ZSpGN242wpXGs")

# Listar todas as abas (worksheets)
abas = spreadsheet.worksheets()
print([aba.title for aba in abas])  # Ver os nomes das abas

"""
# Selecionar uma aba pelo nome
aba = spreadsheet.worksheet("Abril/2025")

# Alterar um valor em uma célula (exemplo: A1)
aba.update('A1', 'Novo valor')

# Adicionar uma nova aba
spreadsheet.add_worksheet(title="Nova Aba", rows="100", cols="20")

# Renomear uma aba
aba.update_title("Nome Novo da Aba")

# Deletar uma aba
# spreadsheet.del_worksheet(aba)
"""