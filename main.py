import pandas 
import quine

def resultados(Data):
  global QA, Qf, variaveis, nbits, varcontrl, sizecont
  nvariaveis = nbits+varcontrl

  enderecos = []
  for i in range(2**nvariaveis):
    enderecos.append('{0:b}'.format(int(i)).zfill(nvariaveis))

  for i in variaveis:
    tabletrue = ['X']*(2**nvariaveis) 
    for j in range(sizecont):
      adr = enderecos.index(QA[j])
      tabletrue[adr] = Data[i][j]
    print(i, end = " = ")
    print(quine.mccluskey(nvariaveis, tabletrue))
  print()
  pass
def SaidasQ():
  global QA, Qf, Data, variaveis, nbits, varcontrl
  bit = 0
  c = 0
  while c < nbits+varcontrl:
    Data[str(variaveis[bit])] = []
    Data[str(variaveis[bit+1])] = []
    global sizecont
    for i in range(sizecont):
      if (QA[i][c] == '0') and (Qf[i][c] == '0'):
        Data[str(variaveis[bit])].append('0')
        Data[str(variaveis[bit+1])].append('X')
      elif (QA[i][c] == '0') and (Qf[i][c] == '1'):
        Data[str(variaveis[bit])].append('1')
        Data[str(variaveis[bit+1])].append('X')
      elif (QA[i][c] == '1') and (Qf[i][c] == '0'):
        Data[str(variaveis[bit])].append('X')
        Data[str(variaveis[bit+1])].append('1')
      else:
        Data[str(variaveis[bit])].append('X')
        Data[str(variaveis[bit+1])].append('0')
    bit += 2
    c+=1
  pass
def principal():
  global nbits, contagem, control, QA, Qf, Data, varcontrl
  print()
  # varcontrl = 2
  # nbits = 4
  # contagem = '0874289246507354579483'
  varcontrl = int(input("Bits de Controle: "))
  nbits = int(input("Bits de Contagem: "))
  contagem = str(input("Contagem: "))
  global sizecont
  sizecont = len(contagem)
  possiveis = [0]*10
  for i in range(sizecont):
    repeticao = possiveis[int(contagem[i])]
    control.append('{0:b}'.format(int(repeticao)).zfill(varcontrl))
    possiveis[int(contagem[i])] += 1

  for i in range(sizecont):
    QA.append('{0:b}'.format(int(contagem[i])).zfill(nbits))
  
  for i in range(sizecont):
    QA[i] = control[i] + QA[i]

  for i in range(len(QA)):
    if i == len(QA)-1:
      Qf.append(QA[0])
    else:
      Qf.append(QA[i+1])

  Data["QA"] = QA
  Data["QF"] = Qf
  global variaveis
  var = ''
  for i in range(nbits+varcontrl):
    var = "J" + chr(65+i)
    variaveis.append(var)
    var = "K" + chr(65+i)
    variaveis.append(var)
  print()
  pass
QA = []
Qf = []
control = []
Data = {}
nbits = 0
sizecont = 0
variaveis = []
principal()
SaidasQ()
Tabela = pandas.DataFrame(Data)
print(Tabela)
print()
resultados(Data)
