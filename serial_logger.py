import serial
import serial.tools.list_ports
import time
import os
from datetime import datetime

BAUDRATES = [1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]


def list_ports():
    ports = serial.tools.list_ports.comports()
    return [p.device for p in ports]


def save_log(port, baudrate, text):

    if not os.path.exists("logs"):
        os.makedirs("logs")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"logs/log_{timestamp}_{port}_{baudrate}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Porta: {port}\n")
        f.write(f"Baudrate: {baudrate}\n")
        f.write(f"Data: {datetime.now().isoformat()}\n")
        f.write(f"Preview: {text}\n")

    print("Log criado:", filename)


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

                    # NÃO para o scanner
                    continue

            except:
                continue

    print("\nScan finalizado.")


if __name__ == "__main__":
    scan_ports()