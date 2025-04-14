nome = 'Jao'
serve = 5
Mixer = '11'
NivelMixer = '49'
pavilhao = 204
WasLvl = [10,20,30,40,50]#[int(input('Digite o Nível do Was respectivamente: ')) for values in range(5)]
Diamantes = 1.457
gemas = 124
PedrasDoLune = 3
LivrosAzuis = 2
LivrosVerdes = 2
TriploSpeed = 1
CavPlatinados = 2
Preco = 1900
Parcelamento = '4'

variavel_final = ''
def AddVarFinal(comando):
    global variavel_final
    variavel_final += comando + '\n'
    

def VerificacaoDePosse(texto, objeto):
    return (f'{texto}: {objeto}') if PedrasDoLune >=1 else ''

def Verificacao_de_personagem(personagem):
    questionamento = input(f'Tem o {personagem}? Y or N ')
    if questionamento.upper().startswith('Y'):
        nivel = [1,1,1,1,1]
        conversao = list(map(str, nivel))
        final = ''.join(conversao) 
        AddVarFinal(f'{personagem}: {final}')
        return 
    return 

AddVarFinal((f'Nick: *{nome}* | Servidor: A-{serve}'))
if int(NivelMixer) >= 50:
    AddVarFinal((f'Mixer: {Mixer+'/'+NivelMixer}'))
else:
    AddVarFinal((f'Mixer: {Mixer}'))
AddVarFinal((f'Pavilhão/Visual: Nível {pavilhao}'))
#configurando o WAS
WasLvlConvertido = list(map(str, WasLvl))
AddVarFinal((f'WOS: {' '.join(WasLvlConvertido)}'))
#diamantes
AddVarFinal(f'Diamantes: {float(Diamantes)}')
#gemas
AddVarFinal(f'Gemas: {gemas}')
#pedras
AddVarFinal(f'Pedras do Lune: {PedrasDoLune}') if PedrasDoLune >=1 else ''
AddVarFinal(VerificacaoDePosse('Livros Azuis', LivrosAzuis))
AddVarFinal(VerificacaoDePosse('Livros Verdes', LivrosVerdes))
AddVarFinal(VerificacaoDePosse('Cosmos triple Speed', TriploSpeed))
# Personagens e suas Skills
# Verificacao_de_personagem('Thanatos')
# Verificacao_de_personagem('Oneiros')
# Verificacao_de_personagem('Yohma')
# Verificacao_de_personagem('Exclamação Sapuris')
# Verificacao_de_personagem('Shaka DC')
# Verificacao_de_personagem('Apollo')
##reparos
##
##falta fazer

#cavaleiros platinados
AddVarFinal(f'Cavaleiros Platinados: {CavPlatinados}' if CavPlatinados >= 1 else '')
AddVarFinal('')#espaço

#lembre-se que essa parte aqui é o valor do dolar no momento.
#futuramente, teremos que usar uma api
#ademais, creio que nesse caso, o uso do round seja inapropiado. 
ValorDolar = 5.87
#lembrando que tem que pensar uma forma de encaixar o negoviável
AddVarFinal(f'Valor: {round(Preco/ValorDolar, 2)} USD ou {Preco} BRL')
AddVarFinal('')#espaço
Parcelamento = input('Digite um valor caso haja parelamento. Se não houver, aperte enter. ')
if Parcelamento:
    AddVarFinal(f'Condição de pagamento parcelado em até *{Parcelamento}x*')
    AddVarFinal('') #espaco

AddVarFinal('PDF *Atualizado!*')
AddVarFinal('_Pagamento via Pix, Western Union, Wise, PicPay e outros._')
AddVarFinal('_Entre em contato no PV para mais detalhes._')



print(variavel_final)
 



      
      
      
      
      
      
      
      
      
