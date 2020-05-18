from pynput.keyboard import Key, KeyCode, Listener


class KeyListener(object):
    
    def __init__(self, master_key = ["insert"]):

        """
        @param master_key: Lista com as teclas de atalho.
        """

        self.__master_key = master_key
        self.__master_key_pressed = False
        self.__current_keys = set()
        self.__listener = None


    def __is_master_key_pressed(self):

        """
        Verifica se as combinações da "master_key" estão ativas.
        """

        return all([modifier in self.__current_keys for modifier in self.__master_key])


    def __on_press(self, key):

        """
        Callback para o evento "on_press" do Listener.
        """

        # Verifica se a tecla pressionada está na lista de combinações da "master_key".
        if isinstance(key, Key) and key.name in self.__master_key:
            self.__current_keys.add(key.name)

        # Se a "master_key" estiver ativa será informado que 
        # a callback passada no método "start" poderá ser executada.
        elif self.__is_master_key_pressed():
            self.__master_key_pressed = True
            

    def __on_release(self, key):

        """
        Callback para o evento "on_release" do Listener.
        """

        # Verifica se a tecla não é um modificador e se a "master_key" foi pressionada.
        if isinstance(key, KeyCode) and self.__master_key_pressed: 
            self.__callback(key.char)

        # Verifica se a tecla está na lista de combinações da "master_key". 
        # Se estiver, essa tecla será removida da lista de teclas ativas. 
        if isinstance(key, Key) and key.name in self.__current_keys:
            self.__current_keys.remove(key.name)

        self.__master_key_pressed = False


    def start(self, callback):

        """
        Inicializa o Listener.

        @param callback: Essa função será chamada quando a "master_key"
        for pressionada junto com uma outra tecla que não seja um modificador.
        """

        self.__callback = callback
        self.__listener = Listener(on_press = self.__on_press, on_release = self.__on_release)
        self.__listener.start()


    def stop(self):
        
        """
        Interrompe a execução da Thread.
        """

        if self.__listener and self.__listener.is_alive:
            self.__listener.stop()
            self.__master_key_pressed = False
        
        
