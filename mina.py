Campo = list[list[str]]
Camion = dict[str,int]

def excavar_campo(campo : Campo) -> None:
    for i in range(len(campo)):
        for j in range(len(campo)):
            if campo[i][j] == "L":
                campo[i][j] = "LE"

def preparar_camión(campo : Campo) -> Camion:
    camion = {"litio":0,"nafta":0}
    camion["nafta"] = len(campo)*len(campo[0])
    return camion 

def recuperar_litio(campo : Campo, camion : Camion) -> bool:
    for i in range(len(campo)):
        for j in range(len(campo[i])):
            camion["nafta"] -= 1
            if campo[i][j] == "LE":
                campo[i][j] = ""
                camion["litio"] = 1
            if camion["nafta"] <= 0:
                return False
    return True

def extraer_litio(campos : list[Campo]) -> tuple[int,int,int]:
    litio_extraído = 0
    nafta_utilizada = 0
    for campo in campos:
        excavar_campo(campo)
        camion = preparar_camión(campo)
        exito = recuperar_litio(campo,camion)
        if exito:
            litio_extraído += camion["litio"]
    agua_necesaria = litio_extraído * 2000000
    return litio_extraído, nafta_utilizada, agua_necesaria

if __name__ == "__main__":
    campos = [
        [["L","L",""],
         ["","L",""],
         ["","L",""]],
        [["L","L"],
         ["","L"],
         ["L",""]],
        [["L","L",""],
         ["","L"],
         ["L","","L"]]
    ]
    litio_extraído, nafta_utilizada, agua_necesaria = extraer_litio(campos)
    print(f"Litio extraído: {litio_extraído} toneladas \nNafta utilizada: {nafta_utilizada} tanques \nAgua necesaria: {agua_necesaria} litros")