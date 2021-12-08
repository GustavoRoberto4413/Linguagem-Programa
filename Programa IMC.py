from sqlite3 import connect
conn = connect('banco.db')
curs = conn.cursor()

nome = str(input("Qual seu nome completo? "))
endereco = str(input("Qual seu endereço completo? "))
cpf = str(input("Qual seu CPF? "))
peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (M) "))
imc = peso / (altura ** 2)
print("O IMC dessa pessoa é de %.2f" % (imc))
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está na faixa de peso normal.")
elif 25 <= imc < 30:
    print("Você está em sobrepeso.")
elif 30 <= imc < 40:
    print("Você está em obesidade.")
elif imc >= 40:
    print("Você está em obesidade mórbida.")

curs.execute("insert into tb_paciente (id_paciente, nome, endereco, cpf, peso, altura, imc) values (NULL, ?, ?,?,?,?,?)", (nome, endereco, cpf, peso, altura, imc))


curs.execute("SELECT * FROM tb_paciente;")
for id_paciente, nome, endereco, cpf, peso, altura, imc in curs.fetchall():
    print("Cod: " + str(id_paciente) + "\n")
    print("Paciente: ",  str(nome))
    print("Endereço: ", str(endereco), "\n")
    print(" CPF: ",  str(cpf), "\n")
    print("Peso: ", (peso))
    print("Altura: ", (altura))
    print(f"O IMC dessa pessoa é de:  ", imc)
    print("===========IMC Gustavo Dev=================")



conn.commit()
conn.close()

