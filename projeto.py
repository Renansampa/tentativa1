tarefas = {}
usuarios = {}
def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True
def fazer_login():
    global usuarios
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    if login in usuarios and usuarios[login] == senha:
        print("Login bem sucedido!")
        return True
    else:
        print("Credenciais inválidas.")    
    return False
def fazer_cadastro():
    global usuarios
    novo_login = input("Digite um novo login: ")
    if novo_login in usuarios:
        print("Este login já está em uso. Tente outro.")
        return
    nova_senha = input("Digite uma senha: ")
    usuarios[novo_login] = nova_senha
    print("Cadastro realizado com sucesso.")
def listar_tarefas():
    print("Tarefas pendentes:")
    for id, tarefa in tarefas.items():
        if not tarefa['concluida']:
            print(f"{id}: {tarefa['tarefa']}")
while True:
    print("\n escolha uma opção ")
    print("1. Login.")
    print("2. Cadastrar.")
    print("3. Sair.")        
    escolha = input("Digite o número da opção: ")
    if escolha == '1':
        if fazer_login():
            def adicionar_tarefa():
                tarefa = input("Digite a tarefa: ")
                tarefas[len(tarefas) + 1] = {'tarefa': tarefa, 'concluida': False}
                print("Tarefa adicionada com sucesso!")

            def marcar_como_concluida():                     
                listar_tarefas()
                tarefa_id = input("Digite o ID da tarefa concluída: ") 
                if isnumber(tarefa_id):

                    if tarefa_id in tarefas and not tarefas[tarefa_id]['concluida']:
                        tarefas[tarefa_id]['concluida'] = True
                        print("Tarefa marcada como concluída.")          
                    else:
                        print("Tarefa não encontrada ou já concluída.")
                else:
                    print("input invalido")
            def excluir_tarefa():
                listar_tarefas()
                tarefa_id = input("Digite o ID da tarefa a ser excluída: ")
                if isnumber(tarefa_id):
                    if tarefa_id in tarefas:
                        del tarefas[tarefa_id]
                        print("Tarefa excluída com sucesso.")
                    else:
                        print("Tarefa não encontrada.")
                else:
                    print("input invalido")        
            while True:
                print("\nEscolha uma opção:")
                print("1. Adicionar Tarefa")
                print("2. Listar Tarefas Pendentes")
                print("3. Marcar Tarefa como Concluída")
                print("4. Excluir Tarefa")
                print("5. Sair da conta")        
                escolha = input("Digite o número da opção: ")                
                if escolha == '1':
                    adicionar_tarefa()
                elif escolha == '2':
                    listar_tarefas()
                elif escolha == '3':
                    marcar_como_concluida()
                elif escolha == '4':
                    excluir_tarefa()
                elif escolha == '5':
                    print("até a proxima")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
        else:
            continue
    elif escolha == '2':
        fazer_cadastro()
        continue
    elif escolha == '3':
        print("saindo do programa.")
        break
    else:
        print("escolha indisponivel, por favor tente outra")
        continue
