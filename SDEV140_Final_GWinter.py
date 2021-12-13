'''
Program: SDEV140_Final_GWinter.py
Author:  George Winter
Date:    December 13, 2021
Summary: Final Project, create a GUI for a random item generator in D&D
'''

from tkinter import *
import random

class ItemGUI:
    def __init__(self):
        #set main window
        self.main_window = Tk()
        self.main_window.title("Random Item Generator")
        self.main_window.geometry("300x350")

        # Create frames
        self.top_frame    = Frame(self.main_window)
        self.second_frame = Frame(self.main_window)
        self.third_frame  = Frame(self.main_window)
        self.fourth_frame = Frame(self.main_window)
        self.fifth_frame  = Frame(self.main_window)
        
        # Create drop down button for challenge rating
        self.CR_label = Label(self.top_frame, text="Challenge Rating: ")

        self.CR_options = ['Choose a Challenge Rating','level 0-4','level 5-10',\
                      'level 11-16','level 17+']
        self.CR_clicked = StringVar(self.main_window)
        self.CR_clicked.set(self.CR_options[0])
        self.CR_drop = OptionMenu(self.top_frame,self.CR_clicked,*self.CR_options)
        
        self.CR_label.pack(side="left")
        self.CR_drop.pack(side="left")

        # Create drop down button for type of treasure
        self.TT_label = Label(self.second_frame, text="Treasure Type: ")

        self.treasure_type = ['Choose a Treasure Type','Individual','Gold Only',\
                         'Magic Items Only','Hoard']
        self.TT_clicked = StringVar(self.main_window)
        self.TT_clicked.set(self.treasure_type[0])
        self.TT_drop = OptionMenu(self.second_frame,self.TT_clicked,*self.treasure_type)

        self.TT_label.pack(side="left")
        self.TT_drop.pack(side="left")

        # Create a Run and Quit buttons
        self.run_prog    = Button(self.third_frame,text="Run", \
                           command=self.set_vars)
        self.quit_button = Button(self.third_frame,text="Quit", \
                           command=self.main_window.destroy)

        self.run_prog.pack(side="left",padx=10)
        self.quit_button.pack(side="left",padx=10)

        # Create output label
        self.output_label = Label(self.fourth_frame, text="Loot Rewarded:")
        self.output_label.pack()

        # Create an output box
        self.output = StringVar()
        self.loot_output = Label(self.fifth_frame,textvariable = self.output,borderwidth=2, \
                                 relief="solid", padx = 10)
        self.loot_output.pack()

        # Pack frames and run
        self.top_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack(pady=10)
        self.fourth_frame.pack(pady=5)
        self.fifth_frame.pack()
        mainloop()

    # Set input variables
    def set_vars(self):
        CR_out = self.CR_clicked.get()
        TT_out = self.TT_clicked.get()
        
        if CR_out == 'Choose a Challenge Rating':
            CR_var = 1
        elif CR_out == 'level 0-4':
            CR_var = 2
        elif CR_out == 'level 5-10':
            CR_var = 3
        elif CR_out == 'level 11-16':
            CR_var = 4
        elif CR_out == 'level 17+':
            CR_var = 5
        else:
            CR_var = "invalid"

        if TT_out == 'Choose a Treasure Type':
            TT_var = 1
        elif TT_out == 'Individual':
            TT_var = 2
        elif TT_out == 'Gold Only':
            TT_var = 3
        elif TT_out == 'Magic Items Only':
            TT_var = 4
        elif TT_out == 'Hoard':
            TT_var = 5
        else:
            TT_var = "invalid"

        # randomized loot generator
        gold  = ""
        gems  = ""
        art   = ""
        magic = ""
        # CR_var == 2 table, lv 0-4
        if CR_var == 2 and TT_var == 2: #ind
            gold  = str(random.randint(0,6))+"pp "+str(random.randint(3,18))+"gp "+\
                    str(random.randint(4,24))+"sp "+str(random.randint(5,30))+"cp \n"
            gems  = str(random.randint(0,5))+" gem(s) worth "+str(random.randrange(10,21,5))+\
                    "gp each \n"
            art   = str(random.randint(0,3))+" art object(s) worth "+\
                    str(random.randrange(10,26,5))+"gp each \n"
            magic = "none"
        elif CR_var == 2 and TT_var == 3: #GO
            gold  = str(random.randint(0,6))+"pp "+str(random.randint(3,18))+"gp "+\
                    str(random.randint(4,24))+"sp "+str(random.randint(5,30))+"cp \n"
            gems  = "none \n"
            art   = "none \n"
            magic = "none"
        elif CR_var == 2 and TT_var == 4: #MO
            gold  = "none \n"
            gems  = "none \n"
            art   = "none \n"
            magic = str(random.randint(1,4))+" common magic item(s) \n"+\
                    str(random.randint(0,2))+" uncommon magic item(s)"
        elif CR_var == 2 and TT_var == 5: #hoard
            gold  = str(random.randint(0,10))+"pp "+str(random.randint(2,12)*10)+"gp "+\
                    str(random.randint(3,18)*100)+"sp "+str(random.randint(5,30)*100)+"cp \n"
            gems  = str(random.randint(0,5))+" gem(s) worth "+str(random.randrange(10,21,5))+\
                    "gp each \n"
            art   = str(random.randint(0,3))+" art object(s) worth "+\
                    str(random.randrange(10,26,5))+"gp each \n"
            magic = str(random.randint(1,4))+" common magic item(s) \n"+\
                    str(random.randint(0,2))+" uncommon magic item(s)"
            
        # CR_var == 3 table, lv 5-10
        if CR_var == 3 and TT_var == 2: #ind
            gold  = str(random.randint(3,18))+"pp "+str(random.randint(3,12)*10)+"gp "+\
                    str(random.randint(4,25)*10)+"sp "+str(random.randint(5,20)*100)+"cp \n"
            gems  = str(random.randint(2,10))+" gem(s) worth "+str(random.randrange(25,101,25))+\
                    "gp each \n"
            art   = str(random.randint(0,4))+" art object(s) worth "+\
                    str(random.randrange(50,251,50))+"gp each \n"
            magic = "none"
        elif CR_var == 3 and TT_var == 3: #GO
            gold  = str(random.randint(3,18))+"pp "+str(random.randint(3,12)*10)+"gp "+\
                    str(random.randint(4,25)*10)+"sp "+str(random.randint(5,20)*100)+"cp \n"
            gems  = "none \n"
            art   = "none \n"
            magic = "none"
        elif CR_var == 3 and TT_var == 4: #MO
            gold  = "none \n"
            gems  = "none \n"
            art   = "none \n"
            magic = str(random.randint(1,6))+" common magic item(s) \n"+\
                    str(random.randint(1,4))+" uncommon magic item(s) \n"+\
                    str(random.randint(0,2))+" rare magic item(s)"
        elif CR_var == 3 and TT_var == 5: #hoard
            gold  = str(random.randint(3,18)*10)+"pp "+str(random.randint(5,30)*100)+"gp "+\
                    str(random.randint(2,12)*1000)+"sp "+str(random.randint(5,20)*100)+"cp \n"
            gems  = str(random.randint(2,10))+" gem(s) worth "+str(random.randrange(25,101,25))+\
                    "gp each \n"
            art   = str(random.randint(0,4))+" art object(s) worth "+\
                    str(random.randrange(50,251,50))+"gp each \n"
            magic = str(random.randint(1,6))+" common magic item(s) \n"+\
                    str(random.randint(1,4))+" uncommon magic item(s) \n"+\
                    str(random.randint(0,2))+" rare magic item(s)"

        # CR_var == 4 table, lv 11-16
        if CR_var == 4 and TT_var == 2: #ind
            gold  = str(random.randint(2,12)*10)+"pp "+str(random.randint(2,12)*100)+"gp "+\
                    str(random.randint(4,25)*100)+"sp \n"
            gems  = str(random.randint(2,20))+" gem(s) worth "+\
                    str(random.randrange(250,1001,250))+"gp each \n"
            art   = str(random.randint(0,8))+" art object(s) worth "+\
                    str(random.randrange(250,751,250))+"gp each \n"
            magic = "none"
        elif CR_var == 4 and TT_var == 3: #GO
            gold  = str(random.randint(2,12)*10)+"pp "+str(random.randint(2,12)*100)+"gp "+\
                    str(random.randint(4,25)*100)+"sp \n"
            gems  = "none \n"
            art   = "none \n"
            magic = "none"
        elif CR_var == 4 and TT_var == 4: #MO
            gold  = "none \n"
            gems  = "none \n"
            art   = "none \n"
            magic = str(random.randint(2,10))+" common magic item(s) \n"+\
                    str(random.randint(1,6))+" uncommon magic item(s) \n"+\
                    str(random.randint(1,4))+" rare magic item(s) \n"+\
                    str(random.randint(0,2))+" very rare magic item(s)"
        elif CR_var == 4 and TT_var == 5: #hoard
            gold  = str(random.randint(5,30)*100)+"pp "+str(random.randint(5,25)*1000)+"gp \n"
            gems  = str(random.randint(2,20))+" gem(s) worth "+\
                    str(random.randrange(250,1001,250))+"gp each \n"
            art   = str(random.randint(0,8))+" art object(s) worth "+\
                    str(random.randrange(250,751,250))+"gp each \n"
            magic = str(random.randint(2,10))+" common magic item(s) \n"+\
                    str(random.randint(1,6))+" uncommon magic item(s) \n"+\
                    str(random.randint(1,4))+" rare magic item(s) \n"+\
                    str(random.randint(0,2))+" very rare magic item(s)"

        # CR_var == 5 table, lv 17+
        if CR_var == 5 and TT_var == 2: #ind
            gold  = str(random.randint(1,12)*100)+"pp "+str(random.randint(1,6)*1000)+"gp \n"
            gems  = str(random.randint(3,10))+" gem(s) worth "+\
                    str(random.randrange(1000,5001,500))+"gp each \n"
            art   = str(random.randint(0,6))+" art object(s) worth "+\
                    str(random.randrange(2500,5001,1250))+"gp each \n"
            magic = "none"
        elif CR_var == 5 and TT_var == 3: #GO
            gold  = str(random.randint(1,12)*100)+"pp "+str(random.randint(1,6)*1000)+"gp \n"
            gems  = "none \n"
            art   = "none \n"
            magic = "none"
        elif CR_var == 5 and TT_var == 4: #MO
            gold  = "none \n"
            gems  = "none \n"
            art   = "none \n"
            magic = str(random.randint(3,15))+" common magic item(s) \n"+\
                    str(random.randint(1,8))+" uncommon magic item(s) \n"+\
                    str(random.randint(1,6))+" rare magic item(s) \n"+\
                    str(random.randint(1,4))+" very rare magic item(s)\n"+\
                    str(random.randint(0,2))+" legendary magic item(s)"
        elif CR_var == 5 and TT_var == 5: #hoard
            gold  = str(random.randint(8,45)*1000)+"pp "+str(random.randint(12,70)*1000)+"gp \n"
            gems  = str(random.randint(3,10))+" gem(s) worth "+\
                    str(random.randrange(1000,5001,500))+"gp each \n"
            art   = str(random.randint(0,6))+" art object(s) worth "+\
                    str(random.randrange(2500,5001,1250))+"gp each \n"
            magic = str(random.randint(3,15))+" common magic item(s) \n"+\
                    str(random.randint(1,8))+" uncommon magic item(s) \n"+\
                    str(random.randint(1,6))+" rare magic item(s) \n"+\
                    str(random.randint(1,4))+" very rare magic item(s)\n"+\
                    str(random.randint(0,2))+" legendary magic item(s)"
            
        # Error check
        if CR_var == 1 or TT_var == 1:
            self.show = "Incorrect entry, please choose a correct \n"\
                        "Challenge Rating and Treasure Type \n"\
                        "from the dropdown menus."
        else:
            self.show = ('\n Currency: '+   gold+ "\n"+ \
                        'Gems: '+        gems+ "\n"+ \
                        'Art Objects: '+ art+ "\n"+ \
                        'Magic Items: '+ magic+ "\n")
        self.output.set(self.show)

run = ItemGUI()
