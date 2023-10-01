# # Functions  -----> Code Usability

# main()
# {
#     Rishita();   # FUnc. Calling
#     Rishita();   # FUnc. Calling
#     Rishita();   # FUnc. Calling
#     Rishita();   # FUnc. Calling
#     Rishita();   # FUnc. Calling
# }


# def Rishita():    # Func. Defination
#     dvdv
#     dfv
#     df
#     vd
#     fv
#     divmodvd

# Rishita()


# Prefined Func.  ------> print(),  input(),  raw_input(),  len()



# Type - 1   without Return Type and Without Args.

def Muskan():
    print(90 + 23)

Muskan()   # 113


def Kru():
    x,y = 'Aman', 2
    print(x*y)

Kru()


x = 90  # Global Variable

def Demo():
    x = 80   # Local Var.

    x+=10
    print(x)   # 90

Demo()   # 90
x+=22 
print(x+10)   # 122
print(x)     # 112


# --------------------------------
x = 90  # Global Variable

def Demo():
    global x
    x+=10
    print(x)   # 100

Demo()   # 100
x+=22    # 122
print(x+10)   # 132
print(x)     # 122



def kru1():
    def Ajay():
        print('Ajay Function')
    Ajay()
    return
    
print(kru1())   # Ajay Function   None


# -----------------------------------------------------


def Royal(Aman):
    def Techno(Hardik):
        print('Techno Function')
        return Hardik()
    return Techno(Aman)


def MadhuSir():
    print('MadhuSir Function')

Royal(MadhuSir)