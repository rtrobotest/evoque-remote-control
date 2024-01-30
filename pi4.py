import subprocess
import can
from flask import Flask, render_template, request

app = Flask(__name__)

def send_can_message(can_id, data):
    can_interface = 'can0'
    command = "sudo /sbin/ip link set can0 up type can bitrate 500000"
    subprocess.run(command, shell=True, check=True)
    print("CAN interface configured successfully.")

    bus = can.interface.Bus(channel=can_interface, bustype='socketcan')

    message = can.Message(arbitration_id=can_id, data=data, extended_id=False)

    bus.send(message)
    print(f"CAN message sent with ID {can_id} and data {data}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    frame = int(request.form['frame'])
    if frame == 1:
        send_can_message(0x7DF, [0x02, 0x01, 0xFF])
    elif frame == 2:
        send_can_message(0x7DF, [0x02, 0x01, 0xFF])
    elif frame == 3:
        send_can_message(0x7DF, [0x02, 0x01, 0xFF])
    elif frame == 4:
        send_can_message(0x7DF, [0x02, 0x01, 0xFF])
    elif frame == 5:
        send_can_message(0x7DF, [0x02, 0x01, 0xFF])
    elif frame == 6:
        send_can_message(0x7DF, [0x02, 0x01, 0xFF])

    return "CAN message sent successfully!"

if __name__ == '__main__':
    app.run(host='192.168.1.104', port=80, debug=True)