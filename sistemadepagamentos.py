print("Bem-vindo ao sistema de pagamentos!")
tipodepagamento = input("Escolha o tipo de pagamento:\n1-Boleto\n2-Carnê\n3-Cartão\n")
if tipodepagamento == "1":
    valorBoleto = float(input("Digite aqui o valor do seu boleto:\t"))
    tipodeboleto = input("Considerando os tipos de boleto abaixo\n1-Em dia\n2-Atrasado\nDigite o tipo do seu boleto:\t")
    if tipodeboleto == "1":
        print(f"Pronto! Seu boleto no valor de {valorBoleto} foi pago!")
    elif tipodeboleto == "2":
        print("Puxa! Seu boleto venceu. Por favor, gere um novo no sistema.")
elif tipodepagamento == "2":
    valorCarne = float(input("Por favor, digite o valor do seu carnê:\t"))
    tipodecarne = input("Considerando os tipos de carne abaixo\n1-Dia exato\n2-Atrasado\n3-Adiantar parcela\nDigite o tipo do seu carnê:\t")
    if tipodecarne == "1":
        print(f"Pronto! Seu carnê no valor de {valorCarne} foi pago!")
    elif tipodecarne == "2":
        valorCarne = valorCarne + (valorCarne * 10) / 100
        print(f"Pronto! Seu carnê foi pago com multa de 10%, ficando no valor de {valorCarne}.")
    elif tipodecarne == "3":
        valorCarne = valorCarne - (valorCarne * 15) / 100
        print(f"Pronto! Seu carnê foi pago adiantado, ficando no valor de {valorCarne}.")
elif tipodepagamento == "3":
    print("Sentimos muito, mas pagamentos por cartão estão sendo implementados ainda. Agradecemos a compreensão. Saindo...")
else:
    print("Oops! Esta opção não é válida. Saindo...")
