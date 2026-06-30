import segno
import os

BASE_URL = "https://yourdomain.com/qr"

rooms = []

# JHS Rooms
for i in range(1, 11):
    rooms.append(f"JHS-{i:02}")

# SHS Rooms
for i in range(1, 14):
    rooms.append(f"SHS-{i:02}")

os.makedirs("qrcodes", exist_ok=True)

for room in rooms:
    qr = segno.make(f"{BASE_URL}/{room}")
    qr.save(f"qrcodes/{room}.png", scale=10)

print("All QR Codes generated successfully!")