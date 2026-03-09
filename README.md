# Porta Serial Reader

Ferramenta em Python para **detectar automaticamente portas seriais (COM), ler dados recebidos e registrar tudo em arquivos de log**.

O programa varre múltiplas portas seriais, tenta conectar e continua monitorando todas as portas encontradas sem interromper o processo.

Ideal para:

- Testar leitores seriais
- Debug de dispositivos RS232 / USB Serial
- Capturar dados enviados por equipamentos industriais
- Diagnóstico de comunicação serial

---

# Funcionalidades

- Varre automaticamente portas seriais disponíveis
- Tenta conexão em várias portas
- Continua testando todas as portas mesmo após encontrar dados
- Registra todas as leituras em arquivos de log
- Cria automaticamente a pasta `logs`
- Pode ser executado como **script Python** ou **executável (.exe)**

---

# Estrutura do Projeto

```
PortaSerial-Reader
│
├── serial_logger.py
├── build_installer.py
├── serial_logger.spec
├── requirements.txt
├── .gitignore
└── logs/
```

Arquivos principais:

- `serial_logger.py` → script principal que lê as portas seriais
- `build_installer.py` → script que gera o executável
- `serial_logger.spec` → configuração do PyInstaller
- `requirements.txt` → dependências do projeto

---

# Requisitos

- Python **3.10 ou superior**
- Windows (testado)
- Dispositivo conectado em porta serial

---

# Criando o Ambiente Virtual (venv)

No diretório do projeto execute:

```bash
python -m venv venv
```

Ative o ambiente virtual.

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Quando ativo aparecerá algo como:

```
(venv) C:\seu\projeto>
```

---

# Instalando as Dependências

Com o ambiente virtual ativo execute:

```bash
pip install -r requirements.txt
```

Biblioteca principal utilizada:

- `pyserial`

---

# Executando o Programa

Execute:

```bash
python serial_logger.py
```

O programa irá:

1. Detectar portas seriais disponíveis
2. Tentar conectar em cada uma
3. Escutar dados recebidos
4. Criar arquivos de log automaticamente

---

# Logs

Os logs são salvos automaticamente na pasta:

```
logs/
```

Exemplo:

```
logs/
COM3_2024-06-01.log
COM4_2024-06-01.log
```

Cada arquivo corresponde a uma porta serial.

Formato típico do log:

```
[2024-06-01 14:23:10] COM3 -> DATA RECEIVED
```

---

# Gerando o Executável (.exe)

Para gerar um executável standalone utilize **PyInstaller**.

Primeiro instale:

```bash
pip install pyinstaller
```

Depois execute:

```bash
python build_installer.py
```

ou:

```bash
pyinstaller serial_logger.spec
```

Após o build o executável estará em:

```
dist/
```

Exemplo:

```
dist/serial_logger.exe
```

Esse executável pode ser rodado em computadores **sem Python instalado**.

---

# .gitignore

O projeto ignora arquivos desnecessários como:

```
venv/
__pycache__/
*.pyc
logs/
dist/
build/
```

Assim não são enviados ao Git:

- ambiente virtual
- arquivos temporários
- logs
- builds do executável

---

# Como Funciona

O programa realiza os seguintes passos:

1. Lista todas as portas seriais disponíveis
2. Tenta abrir cada porta
3. Monitora dados recebidos continuamente
4. Salva os dados em arquivos de log
5. Continua monitorando todas as portas

Isso permite capturar dados de **múltiplos dispositivos simultaneamente**.

---

# Contribuição

Pull requests são bem-vindos.

Caso queira sugerir melhorias ou encontrou algum problema, abra uma **Issue** no repositório.

---

# Licença

Projeto de uso livre para fins educacionais e diagnóstico de hardware.