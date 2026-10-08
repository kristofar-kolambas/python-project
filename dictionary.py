server = {
    "name":"LAB-1 SERVER",
    "ip":"192.168.1.10",
    "port":8080,
    "is_online":True
}
print("__"*30)

print("server details:",server)
print("Length:",len(server))

print("__"*30)

print(f"server:{server['name']}")
server["os"] = "RedHat Linux"

print("__"*30)

server["port"] = 8000
print(server["port"])

print("__"*30)

for key in server:
    print(key)

print("__"*30)

for value in server.values():
    print(value)

print("__"*30)

for key,value in server.items():
    print(f"{key.upper()} : {value}")