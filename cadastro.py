#Menu principal
while True:
    print('=' * 20)
    print('CADASTRO INTELIGENTE')
    print('=' * 20)

    print('1-Cadastrar pessoa')
    print('2-Ver estatísticas')
    print('3-Sair')

    try:
        opcao_selecionada = int(input('Digite qual opçao deseja realizar: '))
    except ValueError:
        print('Digite apenas numeros inteiros')
    else:
        if opcao_selecionada == 1:
            while True:
                print('Você selecionou o cadastro de usúario.')
            
                cadastro_nome = input('Digite o nome que deseja cadastrar: ')
            
                if not cadastro_nome.strip():
                    print('Digite um nome valido!') 
                else:
                    print('Nome cadastrado!')
                    break


            while True:
                try:
                    cadastro_idade = int(input('Digite a idade da pessoa cadastrada: '))
                except ValueError:
                    print('Digite apenas numero inteiros!')
                else:
                    if cadastro_idade < 0 or cadastro_idade > 120:
                        print('Digite apenas uma idade valida de 0 a 120 anos')
                    else:
                        print('idade do usuario cadastrada!')
                        break
                







        elif opcao_selecionada == 2:
            print('Você deseja ver as eststística de um usúario')
        elif opcao_selecionada == 3:
            print('Você selecionou sair do cadastro')
            break
        else:
            print('Selecione apenas uma das 3 opções!')
        




print('Fim do cadastro!')