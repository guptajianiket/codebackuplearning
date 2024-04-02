import openpyxl

vk1 = openpyxl.load_workbook("C:\\Users\\aniket.gupta\\Desktop\\Diwali Movie Dhamaka - Daily Contest.xlsx")

sh1 = vk1.active

for i in range(1,15):
    c = f"sh1['C{i}']"
    d = f"sh1['D{i}']"
    f = f"sh1['F{i}']"
    g = f"sh1['G{i}']"
    h = f"sh1['H{i}']"
    i1 = f"sh1['I{i}']"
    l = f"sh1['L{i}']"

    c1 = f"EP{i+5}ST"
    d1 = f"EP{i+5}ET"
    f1 = f"EP{i+5}Q"
    g1 = f"EP{i+5}O1"
    h1 = f"EP{i+5}O2"
    i11 = f"EP{i+5}O3"
    l1 = f"EP{i+5}CA"

    z = "="
    y = "update_episode("
    x = f"'Episode {i+5}',"
    w1 = f"{c1}.value,"
    w2 = f"{d1}.value,"
    w3 = f"{f1}.value,"
    w4 = f"{g1}.value,"
    w5 = f"{h1}.value,"
    w6 = f"{i11}.value,"
    w7 = f"{l1}.value)"



    print(y+f"{x}"+w1+w2+w3+w4+w5+w6+"'Blank',"+"'Blank',"+w7)



