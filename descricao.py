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

def VerificacaoDePosse(texto, objeto):
    return (f'{texto}: {objeto}') if PedrasDoLune >=1 else ''

def Verificacao_de_personagem(personagem):
    questionamento = input(f'Tem o {personagem}? Y or N ')
    if questionamento.upper().startswith('Y'):
        print('você agora irá digitar as skills! ')
        nivel = [1,1,1,1,1]
        conversao = list(map(str, nivel))
        final = ' '.join(conversao) 
        return final
    return 

print(f'Nick: *{nome}* | Servidor: A-{serve}')
if int(NivelMixer) >= 50:
    print(f'Mixer: {Mixer+'/'+NivelMixer}')
else:
    print(f'Mixer: {Mixer}')
print(f'Pavilhão/Visual: Nível {pavilhao}')
#configurando o WAS
WasLvlConvertido = list(map(str, WasLvl))
print(f'WOS: {' '.join(WasLvlConvertido)}')
#diamantes
print(f'Diamantes: {float(Diamantes)}')
#gemas
print(f'Gemas: {gemas}')
#pedras
print(f'Pedras do Lune: {PedrasDoLune}') if PedrasDoLune >=1 else ''
print(VerificacaoDePosse('Livros Azuis', LivrosAzuis))
print(VerificacaoDePosse('Livros Verdes', LivrosVerdes))
print(VerificacaoDePosse('Cosmos triple Speed', TriploSpeed))
Verificacao_de_personagem('Thanatos')




 



      
      
      
      
      
      
      
      
      
