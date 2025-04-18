from os import system


nome = input('Nome da Conta: ')
serve = input('Digite apenas a numeração do Serv: ')
##configuração do mixer
possibilididade_mixer = input('você tem Mixer? Y or N ').upper().startswith('Y')
if possibilididade_mixer:
    Mixer = input('Digite Apenas o Mixer:')
    NivelMixer = input('Digite apenas o nível do Mixer: ')
#finalização da configuração do mixer
pavilhao = input('Qual o lvl do Pavilhão/Visual? ')
#Configurando Wos
PossibilidadeWos = input('Tem WOS? Y or N ').upper().startswith('Y') 
if PossibilidadeWos:
    WosLvl = input('Digite o Wos: ').replace(',', '.')
# Finalizando Wos
Diamantes = int(input('Tem quantos diamantes? '))
gemas = input('Tem quantas gemas? ')
PedrasDoLune = int(input('Quantas pedras do lune? '))
LivrosAzuis = int(input('Quantos livros azuis?'))
LivrosVerdes = int(input('Quantos livros verdes? '))
TriploSpeed = int(input('Quantos triploSpeed? '))
CavPlatinados = int(input('Quantos cav Platinados? '))
Preco = int(input('Qual o valor da conta em Brl? '))


#####em manunteção
variavel_final = ''
def AddVarFinal(comando):
    global variavel_final
    variavel_final += comando + '\n'
    

def VerificacaoDePosse(texto, objeto):
    if objeto >=1:
        return AddVarFinal(f'{texto}: {objeto}')
    return

def Verificacao_de_personagem(personagem):
    questionamento = input(f'Tem o {personagem}? Y or N ')
    if questionamento.upper().startswith('Y'):
        #manutenção
        nivel = input('Digite as Skills ')
        AddVarFinal(f'{personagem}: {nivel}')
        return 
    return 
#finaliza
AddVarFinal(f'Conta {nome} à venda! \n')

AddVarFinal((f'Nick: *{nome}* | Servidor: A-{serve}'))
#configuraçãoMixerParte2
if possibilididade_mixer:
    if int(NivelMixer) >= 50:
        AddVarFinal((f'Mixer: {Mixer+'/'+NivelMixer}'))
    else:
        AddVarFinal((f'Mixer: {Mixer}'))
#finalização COnfiMixerTotal
AddVarFinal((f'Pavilhão/Visual: Nível {pavilhao}'))

AddVarFinal((f'WOS: {WosLvl}')) if PossibilidadeWos else ''
#diamantes
AddVarFinal(f'Diamantes: {Diamantes}')
#gemas
AddVarFinal(f'Gemas: {gemas}')
#pedras
AddVarFinal(f'Pedras do Lune: {PedrasDoLune}') if PedrasDoLune >=1 else ''
VerificacaoDePosse('Livros Azuis', LivrosAzuis)
VerificacaoDePosse('Livros Verdes', LivrosVerdes)
VerificacaoDePosse('Cosmos triple Speed', TriploSpeed)
# Personagens e suas Skills
Verificacao_de_personagem('Thanatos')
Verificacao_de_personagem('Oneiros')
Verificacao_de_personagem('Yohma')
Verificacao_de_personagem('Exclamação Sapuris')
Verificacao_de_personagem('Shaka DC')
Verificacao_de_personagem('Apolo')
##reparos
PossibilidadeReparo = input('Tem reparos? Y or N ').upper().startswith('Y')
if PossibilidadeReparo:
    AddVarFinal(f'Reparos: {input('liste os reparos: ')}')


#cavaleiros platinados
AddVarFinal(f'Cavaleiros Platinados: {CavPlatinados}' if CavPlatinados >= 1 else '')
AddVarFinal('')#espaço


#a api aparenta ter funcionado direitinho. Até aqui, creio eu que esteja tudo certo. 
import api_cotacao
ValorDolar = int(api_cotacao.conversao(Preco))



AddVarFinal(f'Valor: {ValorDolar:.2f} USD ou {Preco} BRL')
AddVarFinal('')#espaço
Parcelamento = input('Digite um valor caso haja parcelamento. Se não houver, aperte enter. ')
if Parcelamento:
    AddVarFinal(f'Condição de pagamento parcelado em até *{Parcelamento}x*')
    AddVarFinal('') #espaco

AddVarFinal('PDF *Atualizado!*')
AddVarFinal('') #espaco

AddVarFinal('_Pagamento via Pix, Western Union, Wise, PicPay e outros._')
AddVarFinal('_Entre em contato no PV para mais detalhes._')


system('cls')
print(variavel_final)



##### bugs e futuras correções + funcionalidades :
#não tem a opção de frags de livros
#ainda tá faltando colocar skills de cavaleiros opcionalmente
#ainda não tem a opção de colocar os reparos
#ainda não tem como colocar email substituivel
# futuramente adicionar um corretor para não perder o progresso