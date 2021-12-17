from src.leilao.dominio import Usuario, Lance, Leilao

gui = Usuario('gui')
yuri = Usuario('yuri')

lance_do_yuri = Lance(yuri, 100)
lance_do_gui = Lance(gui, 150)

leilao = Leilao("Celular")

leilao.lances.append(lance_do_yuri)
leilao.lances.append(lance_do_gui)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')
