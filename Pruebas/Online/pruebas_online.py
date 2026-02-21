import pandas as pd

FILE_ID = '1C3JLWUg1FzFE7k7sfxXh-7JWXekyNAqO'
url = f'https://drive.google.com/uc?export=download&id={FILE_ID}'

# Esto te dirá exactamente cómo "ve" Python los nombres de las hojas
excel_file = pd.ExcelFile(url)
print("Las hojas disponibles son:", excel_file.sheet_names)