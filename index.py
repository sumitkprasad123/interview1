

def max_salary_employee(employees ):
    max=0
    global index 
    for i in range(0,len(employees)):
        if employees[i]["salary"]>max :
            max = employees[i]["salary"]
            index = i
    x = employees[index]        
    print(x)



employees = [
    {"name":"Alok","salary":20000,"designation":"developer"},
    {"name":"Rohit","salary":35000,"designation":"operator"},
    {"name":"Amit","salary":10000,"designation":"manager"}
]
max_salary_employee(employees )