class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao
        
class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.cliente = cliente
        self.__set_agencia = agencia
        self.__set_numero = numero
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 // ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia
    
   
    def __set_agencia(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo agencia deve ser um inteiro', value)
        if value <= 0:
            raise ValueError('O atributo agencia deve ser maior que zero')
        
        self.__agencia = value

    @property
    def numero(self):
        return self.__numero
    
   
    def __set_numero(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo numero deve ser um inteiro') 
        if value <= 0:
            raise ValueError('O atributo numero deve ser maior que zero')
        
        self.__numero = value

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            raise ValueError('O atributo saldo deve ser maior que zero')
        if value <= 0:
            raise ValueError('O atributo saldo deve ser maior que zero')
        
        self.__saldo = value  


    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)

    def sacar(self, valor):
        self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

conta_corrente = ContaCorrente('Aline', 500, 25000)
print(conta_corrente.cliente)




    

