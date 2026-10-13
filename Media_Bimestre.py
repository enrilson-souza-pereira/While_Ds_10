def calculo_media(aluno, materia, lista_medias):
    b1 = int(input("Qual a nota do primeiro Bimestre? "))
    b2 = int(input("Qual a nota do segundo Bimestre? "))
    b3 = int(input("Qual a nota do terceiro Bimestre? "))
    b4 = int(input("Qual a nota do quarto Bimestre? "))
    
    soma_dos_bimestres = b1 + b2 + b3 + b4 
    media_bimestre = soma_dos_bimestres / 4
    
    # Adiciona a média na lista específica do aluno
    lista_medias.append(media_bimestre)

    if media_bimestre < 5:
        print(f"O aluno {aluno} deve fazer recuperação de {materia}")
        print(f"A média dele foi {media_bimestre}\n")
    else:
        print(f"O aluno {aluno} foi aprovado em {materia}")
        print(f"A média dele foi {media_bimestre}\n")

# Loop principal para cadastrar vários alunos
continuar_sistema = 0

while continuar_sistema == 0:
    Aluno = input("Qual o nome do Aluno? ")
    
    # Listas exclusivas para o aluno atual
    materias_aluno = []
    medias_aluno = []
    numero_materias = 0
    
    # Loop para cadastrar as matérias do aluno
    loop_materias = 0
    while loop_materias == 0:
        Materia = input("Qual a matéria? ")
        numero_materias += 1
        materias_aluno.append(Materia)
        
        calculo_media(Aluno, Materia, medias_aluno)
        
        sim_nao = int(input("Deseja registrar outra matéria para este aluno? 0 para sim, 1 para não: "))
        
        if sim_nao == 1:
            loop_materias = 1  # Encerra o loop de matérias deste aluno

    # Exibição do relatório final do aluno atual
    print(f"\n--- RELATÓRIO FINAL: {Aluno} ---")
    for i in range(numero_materias):
        print(f"Matéria: {materias_aluno[i]} | Média: {medias_aluno[i]}")
    print("-" * 30)
    
    # Pergunta se quer cadastrar outro aluno
    continuar_sistema = int(input("\nDeseja cadastrar outro aluno? 0 para sim, 1 para sair do sistema: "))

print("\nSistema encerrado. Todos os relatórios foram gerados!")