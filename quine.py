def mccluskey(bits,entradas):

    def VerificaChave(chave, chavedepesquisa):
            incidencia = 0
            valores = []
            termos = chavedepesquisa.split(",")
            if len(termos) > 1:
                primeirovalor = ''
                segundovalor = ''
                for digito in range(len(termos)):
                    valores = []
                    if digito < len(termos) / 2:
                        primeirovalor += termos[digito]
                        if digito != (len(termos) / 2) - 1:
                            primeirovalor += ","
                    else:
                        segundovalor += termos[digito]
                        if digito != len(termos) - 1:
                            segundovalor += ","
                valores.append(primeirovalor)
                valores.append(segundovalor)
            incidencia = valores.count(chave)
            return incidencia
    def Absorsao(equacao):
        absorsao = []
        for i in equacao:
            if i.count(".") != 0:
                AND1 = i.split(".")
            else:
                AND1 = i.split()
            for j in equacao:
                if i != j:
                    if j.count(".") != 0:
                        AND2 = j.split(".")
                        if all(k in AND2 for k in AND1):
                            if all(k in AND1 for k in AND2):
                                break
                            else:
                                absorsao.append(j)
        novaequacao = []
        for i in equacao:
            if i not in absorsao:
                novaequacao.append(i)
        return novaequacao
    def PostuladoAND(AND):
        AND = AND.split(".")
        novoANDlista = []
        for i in AND:
            if i not in novoANDlista:
                novoANDlista.append(i)
        AND = ''
        for i in range(len(novoANDlista)):
            AND += novoANDlista[i]
            if i != len(novoANDlista) - 1:
                AND += "."

        return AND
    def PetrickFinal(Petrick):
        PetrickComparativo = list()
        distributiva = list()
        equacaofinal = []
        indicedoproduto = 0
        while len(Petrick) != 1:
            while len(Petrick) != len(PetrickComparativo):
                if indicedoproduto < len(Petrick):
                    distributiva = Petrick[indicedoproduto]
                    PetrickComparativo.append(Petrick[indicedoproduto])
                    novadistributiva = []
                    if indicedoproduto+1 < len(Petrick):
                        PetrickComparativo.append(Petrick[indicedoproduto+1])
                        for i in range(len(distributiva)):
                            for k in range(len(Petrick[indicedoproduto + 1])):
                                soma = distributiva[i] + "." + Petrick[indicedoproduto+1][k]
                                soma = PostuladoAND(soma)
                                novadistributiva.append(soma)
                    novadistributiva = Absorsao(novadistributiva)
                    equacaofinal.append(novadistributiva)
                    indicedoproduto = len(PetrickComparativo)
                if indicedoproduto >= len(Petrick) and len(Petrick) % 2 != 0:
                    equacaofinal.pop()
                    equacaofinal.append(Petrick[-1])
            Petrick = equacaofinal[:]
            PetrickComparativo = list()
            distributiva = list()
            equacaofinal = []
            indicedoproduto = 0
        final = []
        for i in Petrick[0]:
            if i not in final:
                final.append(i)
        menor = len(final[0])
        menor_ok = final[0]
        for i in range(len(final)):
            if len(final[i]) < menor:
                menor = len(final[i])
                menor_ok = final[i]
        return menor_ok
    def TermosPetrick(PrimeImplicante, BibliotecaPetrick):
        EquacaoPetrick = {}
        equacao = ''
        indicepetrick = 0
        listaequacao = []
        for chave in list(PrimeImplicante.keys()):
            EquacaoPetrick["P%i"%indicepetrick] = chave
            indicepetrick+=1
        for valores in list(BibliotecaPetrick.values()):
            equacao += "("
            soma = []
            for indice in range(len(valores)):
                lista = list(EquacaoPetrick.values())
                i = lista.index(valores[indice])
                equacao += list(EquacaoPetrick.keys())[i]
                soma.append(list(EquacaoPetrick.keys())[i])
                if indice != len(valores) - 1:
                    equacao += " + "
            equacao += ")"
            listaequacao.append(soma)

        return listaequacao, EquacaoPetrick
    def ResultadoFinal(essencialpiextraidos, letras, saidas):
        ExpressaoSimples = ''
        qntde1 = saidas.count('1')
        if all(i == "1" or i == 'x' or i == 'X' for i in saidas) and qntde1 > 0:
            ExpressaoSimples += "1"
        elif all(i == "0" or i == "x" or i == "X" for i in saidas):
            ExpressaoSimples += "0"
        else:
            for binarios in list(essencialpiextraidos.values()):
                for l in range(len(binarios)):
                    if binarios[l] == "1":
                        ExpressaoSimples += letras[l]
                    elif binarios[l] == "0":
                        ExpressaoSimples += letras[l] + u'\u0304'
                if binarios != list(essencialpiextraidos.values())[-1]:
                    ExpressaoSimples += " + "
        return ExpressaoSimples
    def OrganizaPI(primeimplicantes, implicantes):
        organizaPI = {}
        implicantes = implicantes[::-1]
        for ordem in range(len(implicantes)):
            for chave in list(implicantes[ordem].keys()):
                if chave in list(primeimplicantes.keys()):
                    organizaPI[chave] = primeimplicantes[chave]

        return organizaPI
    def MinimizaPrimeImplicantes(minitermoreduzido, primeimplicante):
        primeimplicantereduzido = {}
        for chave in list(primeimplicante.keys()):
            minitermosusados = []
            valoresdachave = chave.split(",")
            confirmacao = True
            for valor in valoresdachave:
                if valor in list(minitermoreduzido.keys()):
                    minitermosusados.append(valor)
            for chavepesquisa in list(primeimplicante.keys()):
                if chave == chavepesquisa:
                    continue
                else:
                    minitermosusadoscp = []
                    for valor in chavepesquisa.split(","):
                        if valor in list(minitermoreduzido.keys()):
                            minitermosusadoscp.append(valor)
                    if all(val in minitermosusadoscp for val in minitermosusados):
                        if len(minitermosusados) < len(minitermosusadoscp):
                            confirmacao = False
                        elif len(minitermosusados) == len(minitermosusados):
                            if chavepesquisa in list(primeimplicantereduzido.keys()):
                                confirmacao = False
            if confirmacao:
                primeimplicantereduzido[chave] = primeimplicante[chave]
        return primeimplicantereduzido
    def EssencialPrimeImplicantes(resultsemdontcare, primeimplicant):
        essencial = {}
        contessencialprime = {}
        termosprime = []
        Petrick = {}
        chavescomminitermosrepetidos = []
        for minitermo in list(resultsemdontcare.keys()):
            contaessencialpi = 0
            chavescomminitermosrepetidos = []
            for chave in list(primeimplicant.keys()):
                if chave.count(minitermo) > 0:
                    listadevalores = []
                    listadevalores = chave.split(",")
                    if listadevalores.count(minitermo) > 0:
                        contaessencialpi += listadevalores.count(minitermo)
                        index = chave
                        chavescomminitermosrepetidos.append(chave)
            contessencialprime[minitermo] = chavescomminitermosrepetidos
            if contaessencialpi == 1:
                essencial[index] = primeimplicant[index]
                termosprime.append(minitermo)
        for chave in list(essencial.keys()):
            if chave in primeimplicant:
                del primeimplicant[chave]
        for chave in list(essencial.keys()):
            valoresdachave = chave.split(",")
            for valor in valoresdachave:
                if valor in list(resultsemdontcare.keys()):
                    del resultsemdontcare[valor]
        Petrick.update(contessencialprime)
        return essencial, primeimplicant, resultsemdontcare, Petrick
    def PricipaisImplicantes(candidatos, repetidos, todosimplicantes):
        principaisimplicantes = {}
        for chave in list(candidatos.keys()):
            chavedividida = chave.split(",")
            dmxchave = len(chavedividida)
            tamanhodabiblioteca = len(todosimplicantes)
            indicedacomparacao = 0
            for ordem in range(len(todosimplicantes)):
                valoraleatorio = list((todosimplicantes[ordem]).keys())[0].split(",")
                dmxvaloraleatorio = len(valoraleatorio)
                if dmxvaloraleatorio == (2*dmxchave):
                    indicedacomparacao = ordem
                    break
            if indicedacomparacao < tamanhodabiblioteca:
                incidencia = 0
                confirmacaoincidencia = 0
                for comparacao in list(todosimplicantes[indicedacomparacao].keys()):
                    incidencia += comparacao.count(chave)
                    if incidencia != 0:
                        confirmacaoincidencia += VerificaChave(chave, comparacao)
                if confirmacaoincidencia == 0:
                    base = list(todosimplicantes[indicedacomparacao].keys())[0]
                    virgulas = base.count(",")
                    for comparacaorep in list(repetidos.keys()):
                        if comparacaorep.count(",") == virgulas:
                            incidencia = comparacaorep.count(chave)
                            if incidencia > 0:
                                confirmacaoincidencia = VerificaChave(chave, comparacaorep)
                                if confirmacaoincidencia != 0:
                                    break
                if confirmacaoincidencia == 0:
                    principaisimplicantes[chave] = candidatos[chave]
        principaisimplicantes = OrganizaPI(principaisimplicantes, ImplicantesGeral)
        return principaisimplicantes
    def Comparacao(minitemos, totaldevariaveis):
        Implicantes = {}
        CandidatosPI = {}
        repetidos = {}
        for i in list(minitemos.values()): # listo os minitermos (valores binarios)
            idxprimeirotermo = list(minitemos.values()).index(i)
            primeirotermo = list(minitemos.keys())[idxprimeirotermo]
            c = i.count("1")  # chamo de 'c' a variavel que contém a quantidade de '1' no numero binario i
            novobinario = ''
            numerodecomparacoes = 0 # se meu minitermo não foi comparavel com nenhum outro minitermo logo eu encontrei um principal implicante
            for j in (minitemos.values()): # listo novamente os minitermos (valores binarios)
                if i != j: # para não precisar agrupar por numero de 1s, faço a comparação com todos os termos. (primeira condicao, precisa ser diferente)
                    idxsegundotermo = list(minitemos.values()).index(j)
                    segundotermo = list(minitemos.keys())[idxsegundotermo]
                    k = j.count("1") # chamo de 'k' a variavel que contém a quantidade de '1' no numero binario j
                    if c == (k-1): # segunda condicao, sabendo o que 'c' e 'k' representam é necessario k seja uma unidade maior que c.
                        novobinario = '' # nessa str() serão armazenados os resultados das comparacões
                        contadordeigualdade = 0
                        for l in range(len(i)):
                            if i[l] != j[l]:
                                novobinario += "-"
                            else:
                                novobinario += str(i[l])
                                contadordeigualdade += 1
                        # nesse bloco avaliamos se nossa str() 'novobinario' pode ser armazenado no dicionário, em seguida é criado o indice que contem o valor
                        if (contadordeigualdade == (totaldevariaveis-1)):
                            numerodecomparacoes += 1
                            indexnovobinario = str(primeirotermo) + "," + str(segundotermo)
                            if (novobinario not in list(Implicantes.values())):
                                Implicantes[indexnovobinario] = novobinario
                            else:
                                indexnovobinario = str(primeirotermo) + "," + str(segundotermo)
                                repetidos[indexnovobinario] = novobinario
            if numerodecomparacoes == 0: # talvez pode ser um implicante primo.
                idxchave = list(minitemos.values()).index(i)
                chave = list(minitemos.keys())[idxchave]
                confirmacao = 0
                for item in list(Implicantes.keys()):
                    confirmacao += item.count(chave)
                if confirmacao == 0:
                    CandidatosPI[chave] = i
        return Implicantes, CandidatosPI, repetidos
    def ClassificaSaidas(possibilidades,resultados):
        ImplicantesOrder = {}
        minitermos = {}
        dontcare = {}
        for i in range(len(resultados)):  # nessa interação são retornados os resultados 'verdadeiros' da tabela verdade;
            if resultados[i] == "1" or resultados[i] == "x" or resultados[i] == "X":
                ImplicantesOrder[str(i)] = possibilidades[i] # em seguida adiciono num dicionário os valores cujo a chave é o numero binario na base 10.
                if resultados [i] == "1":
                    minitermos[str(i)] = possibilidades[i]
                else:
                    dontcare[str(i)] = possibilidades[i]
        return ImplicantesOrder, minitermos
    def Binarios(tamanho):
        tabelaverdade = []
        for i in range(tamanho):
            tabelaverdade.append(str(bin(i))) # a função 'bin' retorna algo parecido com a seguinte sequencia; 0b0, 0b1, 0b10, 0b11 (...)
        for i in range(len(tabelaverdade)):
            tabelaverdade[i] = tabelaverdade[i].replace('0b', '') # remolvendo o prefixo 0b teremos os numeros binarios puros; 0, 1, 10, 11, 100, (...)
        possibilidades = []
        for i in tabelaverdade: # ok, tudo que precisamos agora é complementar os numeros de acordo com a quantidade de variaveis;
            while len(i) < len(tabelaverdade[len(tabelaverdade) - 1]): # enquanto meu 'len(numero)' for menor 'len(maiornumero)' adicione '0' a esqueda;
                i = '0' + i[:len(i)] # se eu tenho 4 variaves; meu numero 1 por exemplo; ficará assim 0001.
            possibilidades.append(i) # Em seguida adiciono em uma lista onde estão ficarão as possibilidas da tabela verdade;
        return possibilidades
    
    letras = []
    totaldevariaveis = bits
    for i in range(totaldevariaveis):
        letras.append(chr(65+i))
    numerodepossibilidades = 2**totaldevariaveis
    possibilidades = Binarios(numerodepossibilidades)
    saidas = entradas
    ImplicantesOrdemZero, minitermos = ClassificaSaidas(possibilidades, saidas)
    Implicantes = ImplicantesOrdemZero
    ImplicantesGeral = []
    equacaofinal = {}
    Interacao = 0
    candidatosprime = {}
    ComparacoesRepetidas = {}
    while len(Implicantes) != 0:
        ImplicantesGeral.append(Implicantes)
        Interacao += 1
        Implicantes, naorelacionados, comparacoesrepetidas = Comparacao(Implicantes, totaldevariaveis)
        candidatosprime.update(naorelacionados)
        ComparacoesRepetidas.update(comparacoesrepetidas)
    PI = PricipaisImplicantes(candidatosprime, ComparacoesRepetidas, ImplicantesGeral)
    EPI, PI, minitermos, ProvaveisPetrick = EssencialPrimeImplicantes(minitermos, PI)
    equacaofinal.update(EPI)
    Interacao = 0
    while len(minitermos) != 0:
        if len(EPI) == 0 and len(PI) != 0:
            LinhaInicialPetrick, Termos = TermosPetrick(PI, ProvaveisPetrick)
            TermosEssencias = PetrickFinal(LinhaInicialPetrick).split(".")
            ExtraidosPetrick = []
            for p in TermosEssencias:
                ExtraidosPetrick.append(Termos[p])
            for chave in ExtraidosPetrick:
                EPI[chave] = PI[chave]
            equacaofinal.update(EPI)
            break
        if len(PI) == 0 and len(EPI) == 0:
            print("Failed")
            minitermos = []
            equacaofinal = {}
            break
        PI = MinimizaPrimeImplicantes(minitermos, PI)
        EPI, PI, minitermos, ProvaveisPetrick = EssencialPrimeImplicantes(minitermos, PI)
        equacaofinal.update(EPI)
    equacaosimples = ResultadoFinal(equacaofinal, letras, saidas)
    return equacaosimples