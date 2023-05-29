def object_in_range(a):
    if a == "pico" or a == "kristi" or a == "Kristi":
        return True
    else: 
        return False

def change_door_status_to(i):
    if i == "open":
        list.append(1)
    else:
        list.append(0)
        
list = []
if (object_in_range("pico")):
    change_door_status_to("close")
else:
    change_door_status_to("open")
for x in list:
    print(str(x))
