from src import App
import json


def create_json_file(filename, data, encoding = "utf-8-sig") -> dict:

    """
    Grava um dicionário dentro de um arquivo JSON.
    """

    with open(filename, "w", encoding = encoding) as file:
        content = json.dumps(data, indent = 4, ensure_ascii = False)
        file.write(content)

    return data


def get_json_from(filename, encoding = "utf-8-sig") -> dict:

    """
    Obtém um dicionário de um arquivo JSON.
    """

    with open(filename, encoding = encoding) as file:
        data = json.loads(file.read())
        return data  


def update_data_from(filename, data, encoding = "utf-8-sig") -> dict:
    
    """
    Obtém um dicionário de um arquivo JSON e atualiza o arquivo.
    """

    data = data.copy()

    try: data.update(get_json_from(filename, encoding = encoding))
    finally: return create_json_file(filename, data, encoding = encoding)


# Nomes de arquivos.
settings_file = "settings.json"
keys_and_emojis_file = "keys_and_emojis.json"

# Default: Configuração do programa.
default_settings = {
    "clipboard": False,
    "master_key": ["insert"]
}

# Default: Teclas e emojis.
default_keys_and_emojis = {
    "z": "( ͡° ͜ʖ ͡°)",
    "x": "¯\\_(ツ)_/¯",
    "c": "(^o^)丿",
    "v": "(づ｡◕‿‿◕｡)づ",
    "b": "(づ￣ ³￣)づ",
    "n": "(ㆆ_ㆆ)",
    "m": "（っ＾▿＾）"
}

# Atualiza as configurações, teclas e emojis.
settings = update_data_from(settings_file, default_settings)
keys_and_emojis = update_data_from(keys_and_emojis_file, default_keys_and_emojis)

# Inicializa o aplicativo.
app = App(settings["master_key"], settings["clipboard"], keys_and_emojis)
app.run()

# Espera até que o usuário pressione alguma tecla para encerrar o programa.
input("Press any key to close.")
app.stop()
