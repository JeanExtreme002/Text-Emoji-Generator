from src.generator import Generator
from src.listener import KeyListener


class App(object):

    """
    Classe principal
    """
    
    def __init__(self, master_key, clipboard, keys_and_emojis = {}):

        """
        @param master_key: Veja a documentação na classe Listener.

        @param clipboard: Veja a documentação na classe Generator.

        @param keys_and_emojis: Dicionário com teclas e emojis.
        """

        self.__master_key = master_key
        self.__clipboard = clipboard
        self.__keys_and_emojis = keys_and_emojis

        self.__emoji_generator = Generator()
        self.__listener = None
          

    def __make_emoji(self, key_pressed):

        """
        Cria emoji de uma determinada tecla.
        """

        key = key_pressed.lower()

        if key in self.__keys_and_emojis:
            emoji = self.__keys_and_emojis[key]
            self.__emoji_generator.generate(emoji, self.__clipboard)


    def get_keys_and_emojis(self):

        """
        Obtém dicionário com teclas e emojis.
        """

        return self.__keys_and_emojis.copy()


    def is_running(self):

        """
        Verifica se a Thread ainda está em execução.
        """

        return self.__listener.is_alive()


    def run(self):

        """
        Inicializa o Listener.
        """

        self.__listener = KeyListener(self.__master_key)
        self.__listener.start(self.__make_emoji)
        

    def stop(self):

        """
        Finaliza a execução da Thread.
        """

        self.__listener.stop()


    def update_keys_and_emojis(self, keys_and_emojis):

        """
        Atualiza as teclas e emojis.

        @param keys_and_emojis: Dicionário com teclas e emojis.
        """

        self.__keys_and_emojis.update(keys_and_emojis)
