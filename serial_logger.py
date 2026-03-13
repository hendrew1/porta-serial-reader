import serial
import serial.tools.list_ports
import time
import os
import sys
import traceback
from datetime import datetime

# força sempre usar o diretório do executável
if getattr(sys, 'frozen', False):
    os.chdir(os.path.dirname(sys.executable))
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

BAUDRATES = [1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]


def list_ports():
    ports = serial.tools.list_ports.comports()
    return [p.device for p in ports]


def save_log(port, baudrate, text):

    os.makedirs("logs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"logs/log_{timestamp}_{port}_{baudrate}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Porta: {port}\n")
        f.write(f"Baudrate: {baudrate}\n")
        f.write(f"Data: {datetime.now().isoformat()}\n")
        f.write(f"Preview:\n{text}\n")

    print("Log criado:", filename)


def save_error(e):

    os.makedirs("logs", exist_ok=True)

    filename = f"logs/error_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("ERRO FATAL\n\n")
        f.write(str(e))
        f.write("\n\n")
        f.write(traceback.format_exc())

    print("\nErro registrado em:", filename)


def scan_ports():

    ports = list_ports()

    if not ports:
        print("Nenhuma porta serial encontrada")
        return

    print("\nPortas encontradas:")
    for p in ports:
        print(p)

    for port in ports:

        for baud in BAUDRATES:

            try:

                print(f"\nTestando {port} @ {baud}")

                ser = serial.Serial(port, baud, timeout=2)

                time.sleep(2)

                data = ser.read(100)

                ser.close()

                try:
                    text = data.decode("ascii", errors="ignore").strip()
                except:
                    text = ""

                if len(text) > 3:

                    print("\nDispositivo detectado!")
                    print("Porta:", port)
                    print("Baudrate:", baud)
                    print("Preview:", text)

                    save_log(port, baud, text)

            except Exception:
                continue

    print("\nScan finalizado.")


if __name__ == "__main__":

    try:

        print("Serial Port Scanner iniciado\n")

        scan_ports()

    except Exception as e:

        print("\nERRO FATAL:")
        print(e)
        traceback.print_exc()

        save_error(e)

    finally:

        input("\nPressione ENTER para fechar...")