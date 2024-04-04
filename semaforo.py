import threading
import time
import random

contador_leitor: int = 0
contador_escritor: int = 0
lsinal = threading.Semaphore()
esinal = threading.Semaphore()

def ler_escrever(funcao: str, id: int) -> None:
    """Faz um ciclo finito de receber uma thread, bloqueando outras.\n
    Executa a função conforme o valor do parametro e desbloqueia outras threads."""
    global contador_leitor, contador_escritor
    
    if funcao == "leitor": # Recurso
        while contador_escritor > 0:
            continue 
        
        lsinal.acquire(blocking=False) # Solicita o recurso
        contador_leitor += 1
        print(f"Leitor ID [{id}] -> está lendo... ESCRITORES: {contador_escritor}\nLEITORES: {contador_leitor}\n\n")
        contador_leitor -= 1
        lsinal.release() # Libera o recurso
    else: # Recurso
        while contador_leitor > 0:
            continue 
        
        esinal.acquire(blocking=True) # Solicita o recurso
        # time.sleep(0.25) # espera 1 segundo antes de continuar a execução do código
        contador_escritor += 1
        print(f"Escritor ID [{id}] -> está alterando... ESCRITORES: {contador_escritor}\nLEITORES: {contador_leitor}\n\n")
        contador_escritor -= 1
        esinal.release() # Libera o recurso


def main() -> None:
    """Executa 5 processos, com cada processo tendo 50% de chance de ser leitor ou escritor.
    Os processos são feitos em threads individuais."""
    
    for pessoa in range(5):
        th = threading.Thread(target=ler_escrever, args=(random.choices(["leitor", "escritor"], [5, 5])[0], pessoa))
        th.start()
        

main()