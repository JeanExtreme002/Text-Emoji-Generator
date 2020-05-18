from pynput.keyboard import Controller, Key
import pyperclip


class Generator(object):

    def __init__(self):

        self.__controller = Controller()


    def generate(self, emoji, clipboard = False):

        """
        Digita ou copia um emoji para a área de transferência.

        @param emoji: String com um emoji para ser gerado.

        @param clipboard: Se True, o emoji será copiado para a
        área de transferência. Se False, o emoji será digitado.
        """

        if not clipboard:
            self.__controller.press(Key.backspace)
            self.__controller.type(emoji)

        else:
            pyperclip.copy(emoji)

        return emoji
