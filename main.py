import pandas
import quine

def resultados():
  global QA, Qf, Data, variaveis, nbits
  for i in variaveis:
    print(i, end = " = ")
    print(quine.mccluskey(nbits, Data[i]))
  print()
  pass
def SaidasQ():
  global QA, Qf, Data, variaveis, nbits
  bit = 0
  c = 0
  while c < nbits:
    Data[str(variaveis[bit])] = []
    Data[str(variaveis[bit+1])] = []
    global sizecont
    for i in range(2**nbits):
      if (i >= sizecont):
        Data[str(variaveis[bit])].append('X')
        Data[str(variaveis[bit+1])].append('X')
      elif (QA[i][c] == '0') and (Qf[i][c] == '0'):
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
  global nbits, a, QA, Qf, Data
  print()
  nbits = 3
  a = '12547'
  #nbits = int(input("Numero de Bits: "))
  #a = str(input("Contagem: "))
  global sizecont
  sizecont = len(a)
  for i in range(2**nbits):
    if (i < sizecont):
      Qf.append('{0:b}'.format(int(a[i])).zfill(nbits))
    else:
      Qf.append(nbits*'X')

  for i in range(2**nbits):
    if (i < sizecont):
      QA.append('{0:b}'.format(int(i)).zfill(nbits))
    else:
      QA.append(nbits*'X')

  Data["QA"] = QA
  Data["QF"] = Qf
  global variaveis
  var = ''
  for i in range(nbits):
    var = "J" + chr(65+i)
    variaveis.append(var)
    var = "K" + chr(65+i)
    variaveis.append(var)
  print()
  pass
QA = []
Qf = []
Data = {}
nbits = 0
sizecont = 0
variaveis = []
principal()
SaidasQ()
Tabela = pandas.DataFrame(Data)
print(Tabela)
print()
resultados()
