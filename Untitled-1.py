print("O seu personagem viveu na época da República ou na época do Império ?")
resp1 = input().lower()

if resp1 == "republica" or resp1 == "república":
    print("É aliado da República ou dos Separatistas ?")
    resp2 = input().lower()

    if resp2 == "republica" or resp2 == "república":
        print("É ou já foi membro da Ordem Jedi? (Responda Sim ou Não)")
        resp3 = input().lower()

        if resp3 == "sim":
            print("É membro do Conselho Jedi ? (Respenda Sim ou Não)")
            resp4 = input().lower()

            if resp4 == "sim":
                print("O seu personagem é o Mestre Yoda!")
            elif resp4 == "não" or resp4 == "nao":
                print("A sua personagem é a Ashoka Tano!")
            else:
                print("Resposta inválida!")

        elif resp3 == "não" or resp3 == "nao":
            print("Faz parte do Senado ou do Exército da República (Responda Senado ou Exército) ?")
            resp4 = input().lower()

            if resp4 == "senado":
                print("A sua personagem é Padmé Amidala!")
            elif resp4 == "exército" or resp4 == "exercito":
                print("O seu personagem é o Hunter!")
            else:
                print("Resposta inválida!")

        else:
            print("Resposta inválida!")

    elif resp2 == "separatistas":
        print("Usa sabre(s) de luz ? (Responda Sim ou Não)")
        resp3 = input().lower()

        if resp3 == "sim":
            print("É um Sith ? (Responda Sim ou Não)")
            resp4 = input().lower()

            if resp4 == "sim":
                print("O seu personagem é o Conde Dookan!")
            elif resp4 == "não" or resp4 == "nao":
                print("O seu personagem é o General Grievous!")
            else:
                print("Resposta inválida!")

        elif resp3 == "não" or resp3 == "nao":
            print("É caçador de recompensas ou um droid de batalha? (Responda Caçador ou Droid).")
            resp4 = input().lower()

            if resp4 == "caçador" or resp4 == "cacador":
                print("O seu personagem é o Cad Bane!")
            elif resp4 == "droid":
                print("O seu personagem é o Kalani!")
            else:
                print("Resposta inválida!")
        else:
            print("Resposta inválida!")

    else:
        print("Resposta inválida!")


elif resp1 == "império" or resp1 == "imperio":
    print("É aliado da Rebelião ou do Império ?")
    resp2 = input().lower()

    if resp2 == "rebelião" or resp2 == "rebeliao":
        print("É piloto ou membro do senado imperial ? (Responda Piloto ou Senado)")
        resp3 = input().lower()

        if not resp3 == "senado" and resp3 == "piloto":
            print("É Jedi ou Contrabandista ?")
            resp4 = input().lower()

            if resp4 == "jedi":
                print("Seu personagem é Luke Skywalker!")

            elif resp4 == "contrabandista":
                print("O seu personagem é o Han Solo!")

            else:
                print("Resposta inválida!")

        elif not resp3 == "piloto" and resp3 == "senado":
            print("Morreu antes ou depois da queda do Império? (Responda Antes ou Depois)")
            resp4 = input().lower()

            if resp4 == "antes":
                print("O seu personagem é o Bail Organa!")

            elif resp4 == "depois":
                print("Sua personagem é a Leia Organa!")
            
            else:
                print("Resposta inválida!")

        else:
            print("Resposta inválida!")

    elif resp2 == "imperio" or resp2 == "império":
        print("Consegue usar A Força ? (Responda Sim ou Não)")
        resp3 = input().lower()
        
        if resp3 == "sim":
            print("É um Sith ou um Inquisidor ?")
            resp4 = input().lower()

            if resp4 == "sith":
                print("O seu personagem é o Darth Vader!")

            elif resp4 == "inquisidor":
                print("O seu personagem é o Grande Inquisidor!")

            else:
                print("Resposta inválida!")

        elif resp3 == "não" or resp3 == "nao":
            print("É almirante ou agente do Império ?")
            resp4 = input().lower()

            if resp4 == "almirante":
                print("O seu personagem é o Grão Almirante Trawn!")

            elif resp4 == "agente":
                print("O seu personagem é o Agente Kallus!")

            else:
                print("Resposta inválida!")

        else:
            print("Resposta inválida!")
    
    else:
        print("Resposta inválida!")

else:
    print("Resposta inválida!")