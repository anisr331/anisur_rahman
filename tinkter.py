from tkinter.simpledialog import askinteger
from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("800x800")
label1=Label(top, text="Bangla", font=("Courier 22 bold"))
label1.pack
entry1= Entry(top, width= 40)
entry1.focus_set()
entry1.pack()

label2=Label(top, text="English", font=("Courier 22 bold"))
label2.pack()

entry2= Entry(top, width= 40)
entry2.focus_set()
entry2.pack()

label3=Label(top, text="geanrel math", font=("Courier 22 bold"))
label3.pack

entry3= Entry(top, width= 40)
entry3.focus_set()
entry3.pack()

label4=Label(top, text="religion", font=("Courier 22 bold"))
label4.pack

entry4= Entry(top, width= 40)
entry4.focus_set()
entry4.pack() 


label5=Label(top, text="social science", font=("Courier 22 bold"))
label5.pack

entry5= Entry(top, width= 40)
entry5.focus_set()
entry5.pack()

label6=Label(top, text="religion", font=("Courier 22 bold"))
label6.pack

entry6= Entry(top, width= 40)
entry6.focus_set()
entry6.pack()

label7=Label(top, text="physics", font=("Courier 22 bold"))
label7.pack

entry7= Entry(top, width= 40)
entry7.focus_set()
entry7.pack()

label8=Label(top, text="chemistry", font=("Courier 22 bold"))
label8.pack

entry8= Entry(top, width= 40)
entry8.focus_set()
entry8.pack()

label9=Label(top, text="biology", font=("Courier 22 bold"))
label9.pack

entry9= Entry(top, width= 40)
entry9.focus_set()
entry9.pack()



label10=Label(top, text="higher math", font=("Courier 22 bold"))
label10.pack

entry10= Entry(top, width= 40)
entry10.focus_set()
entry10.pack()

def get_value():
    global b, e, gm , r, ss, ict, phy, chem, bio, hm
    b=int(entry1.get())
    e=int(entry2.get())
    gm=int(entry3.get())
    r=int(entry4.gert())
    ss=int(entry5.get())
    ict=int(entry6.get())
    phy=int(entry7.get())
    chem=int(entry8.get())
    bio=int(entry9.get())
    hm=int(entry10.get())
    b_g = ''
    if(b>0 and b < 33 ):
        b_g = 'F'
    elif(b>32 and b < 40):
        b_g = 'D'
    elif(b>39 and b < 50 ):
        b_g = 'C'
    elif(b>49 and b < 60):
        b_g = 'B'

    elif(b>59 and b < 70 ):
        b_g = 'A-'

    elif(b>69 and b < 80):
        b_g = 'A'

    else:
        b_g = 'A+'

    e_g = ''
    if(e>0 and e < 33 ):
        e_g = 'F'
    elif(e>32 and e < 40):
        e_g = 'D'
    elif(e>39 and e < 50 ):
        e_g = 'C'
    elif(e>49 and e < 60):
        e_g = 'B'

    elif(e>59 and e < 70 ):
        e_g = 'A-'

    elif(e>69 and e < 80):
        e_g = 'A'

    else:
        e_g = 'A+'


    gm_g = ''
    if(gm>0 and gm < 33 ):
        gm_g = 'F'
    elif(gm>32 and gm < 40):
        gm_g = 'D'
    elif(gm>39 and gm < 50 ):
        gm_g = 'C'
    elif(gm>49 and gm < 60):
        gm_g = 'B'

    elif(gm>59 and gm < 70 ):
        gm_g = 'A-'

    elif(gm>69 and gm < 80):
        gm_g = 'A'

    else:
        gm_g = 'A+'


    r_g = ''
    if(r>0 and r < 33 ):
        r_g = 'F'
    elif(r>32 and r< 40):
        r_g = 'D'
    elif(r>39 and r < 50 ):
        r_g = 'C'
    elif(r>49 and r< 60):
        r_g = 'B'

    elif(r>59 and r < 70 ):
        r_g = 'A-'

    elif(r>69 and r < 80):
        r_g = 'A'

    else:
        r_g = 'A+'


    ss_g = ''
    if(ss>0 and ss < 33 ):
        ss_g = 'F'
    elif(ss>32 and ss < 40):
        ss_g = 'D'
    elif(ss>39 and ss < 50 ):
        ss_g = 'C'
    elif(ss>49 and ss < 60):
        ss_g = 'B'

    elif(ss>59 and ss < 70 ):
        ss_g = 'A-'

    elif(ss>69 and ss < 80):
        ss_g = 'A'

    else:
        ss_g = 'A+'


    ict_g = ''
    if(ict>0 and ict < 33 ):
        ict_g = 'F'
    elif(ict>32 and ict< 40):
        ict_g = 'D'
    elif(ict>39 and ict < 50 ):
        ict_g = 'C'
    elif(ict>49 and ict< 60):
        ict_g = 'B'

    elif(ict>59 and ict < 70 ):
        ict_g = 'A-'

    elif(ict>69 and ict < 80):
        ict_g = 'A'

    else:
        ict_g = 'A+'


    phy_g = ''
    if(phy>0 and phy < 33 ):
        phy_g = 'F'
    elif(phy>32 and phy < 40):
        phy_g = 'D'
    elif(phy>39 and phy < 50 ):
        phy_g = 'C'
    elif(phy>49 and phy < 60):
        phy_g = 'B'

    elif(phy>59 and phy < 70 ):
        phy_g = 'A-'

    elif(phy>69 and phy < 80):
        phy_g = 'A'

    else:
        phy_g = 'A+'

    chem_g = ''
    if(chem>0 and chem < 33 ):
        chem_g = 'F'
    elif(chem>32 and chem < 40):
        chem_g = 'D'
    elif(chem>39 and chem < 50 ):
        chem_g = 'C'
    elif(chem>49 and chem < 60):
        chem_g = 'B'

    elif(chem>59 and chem < 70 ):
        chem_g = 'A-'

    elif(chem>69 and chem < 80):
        chem_g = 'A'

    else:
        chem_g = 'A+'

    bio_g = ''
    if(bio>0 and bio < 33 ):
        bio_g = 'F'
    elif(bio>32 and bio < 40):
        bio_g = 'D'
    elif(bio>39 and bio < 50 ):
        bio_g = 'C'
    elif(bio>49 and bio < 60):
        bio_g = 'B'

    elif(bio>59 and bio < 70 ):
        bio_g = 'A-'

    elif(bio>69 and bio < 80):
        bio_g = 'A'

    else:
        bio_g = 'A+'


    hm_g = ''
    if(hm>0 and hm < 33 ):
        hm_g = 'F'
    elif(hm>32 and hm < 40):
        hm_g = 'D'
    elif(hm>39 and hm < 50 ):
        hm_g = 'C'
    elif(hm>49 and hm < 60):
        hm_g = 'B'

    elif(hm>59 and hm < 70 ):
        hm_g = 'A-'

    elif(hm>69 and hm < 80):
        hm_g = 'A'

    else:
        hm_g = 'A+'
    Label(top, text="Bangla Grade= "+b_g, font= ('Century 15 bold')).place(relx = 0.3,
                rely = 0.10,
                anchor = 'ne')
    Label(top, text="English Grade= "+e_g, font= ('Century 15 bold')).place(relx = 0.3,
                rely = 0.15,
                anchor = 'ne')
    Label(top, text="Genarel math Grade= "+gm_g, font= ('Century 15 bold')).place(relx = 0.3,
                rely = 0.20,
                anchor = 'ne')
    Label(top, text="Religion Grade= "+r_g, font= ('Century 15 bold')).place(relx = 0.3,
                rely = 0.25,
                anchor = 'ne')
    Label(top, text="social science Grade= "+ss_g, font= ('Century 15 bold')).place(relx = 0.3,
                rely = 0.30,
                anchor = 'ne')
    Label(top, text="ict Grade= "+ict_g, font= ('Century 15 bold')).place(relx = 0.3,
                rely = 0.35,
                anchor = 'ne')
    Label(top, text="physics Grade= "+phy_g, font= ('Century 15 bold')).place(relx = 0.3,
                rely = 0.40,
                anchor = 'ne')
    Label(top, text="chemistry Grade= "+chem_g, font= ('Century 15 bold')).place(relx = 0.3,
                rely = 0.45,
                anchor = 'ne')
    Label(top, text="Biology Grade= "+bio_g, font= ('Century 15 bold')).place(relx = 0.3,
                rely = 0.50,
                anchor = 'ne')
    Label(top, text="Higher math Grade= "+hm_g, font= ('Century 15 bold')).place(relx = 0.3,
                rely = 0.55,
                anchor = 'ne')
B = Button(top, text ="Calculate Grade" , command=get_value)
B.place(x=150,y=600)
top.mainloop()

