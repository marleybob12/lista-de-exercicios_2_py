from areadotriangulo import area_triangulo
from quadrado import area_quadrado

print("Escolha a forma geométrica:")
print("1 - Triângulo")
print("2 - Quadrado")

opcao = int(input("Digite sua opção: "))

match opcao:
    case 1:
        area_triangulo()

    case 2:
        area_quadrado()

    case _:
        print("Opção inválida!")