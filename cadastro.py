#Menu principal
pessoas_cadastradas = []

while True:
    print('=' * 20)
    print('CADASTRO INTELIGENTE')
    print('=' * 20)

    print('1-Cadastrar pessoa')
    print('2-Ver estatísticas')
    print('3-Sair')

    try:#escolha do que vai fazer no sistema
        opcao_selecionada = int(input('Digite qual opçao deseja realizar: '))
    except ValueError:
        print('Digite apenas numeros inteiros')
    else:
        if opcao_selecionada == 1:#Cadastrar o nome do usuario
            while True:#Cadastro do nome
                print('Você selecionou o cadastro de usúario.')
            
                cadastro_nome = input('Digite o nome que deseja cadastrar: ')
            
                if not cadastro_nome.strip():
                    print('Digite um nome valido!') 
                else:
                    print('Nome cadastrado!')
                    break


            while True:
                try:#Cadastro da idade
                    cadastro_idade = int(input('Digite a idade da pessoa cadastrada: '))
                except ValueError:
                    print('Digite apenas numero inteiros!')
                else:
                    if cadastro_idade < 0 or cadastro_idade > 120:
                        print('Digite apenas uma idade valida de 0 a 120 anos')
                    else:
                        print('idade do usuario cadastrada!')
                        clasificação = ''
                        if 0 <= cadastro_idade < 18:
                            clasificação = 'Menor de idade'
                        elif 18 <= cadastro_idade <60:
                            clasificação = 'Adulto'
                        else:
                            clasificação = 'Idoso'   
                    
                        break
                        
            #guardar o cadastro em um dicionario para ter essas informações depois 
            pessoa = {
                "Nome": cadastro_nome,
                "idade": cadastro_idade, 
                "Caracteristica": clasificação
            }
            pessoas_cadastradas.append(pessoa)







        elif opcao_selecionada == 2:
            print('Você deseja ver as eststística de um usúario')
            print(f'Todas as pessoas cadastradas: {pessoas_cadastradas}')
        elif opcao_selecionada == 3:
            print('Você selecionou sair do cadastro')
            break
        else:
            print('Selecione apenas uma das 3 opções!')
        




print('Fim do cadastro!')