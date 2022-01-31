from GRPgraph import py2D
import random
import time

win = py2D.Screen_([450,600])
run = True
run1 = True
run_poly = True



corabl = py2D.Img_('plain.png')
ploxysh_1 = py2D.Img_('ploxoy_1.png')
ploxysh_2 = py2D.Img_('ploxoy_2.png')
buly = py2D.Img_('puly.png')
bax1 = py2D.Img_('bax1.png')
bax2 = py2D.Img_('bax2.png')
bax3 = py2D.Img_('bax3.png')
bax_set = [bax1,bax2,bax3]
bg = py2D.Img_('bg.png')
bg.Scale([700,850])
bgx = 0
bgy = 0

key = py2D.Sub_.Bord()
mous = py2D.Sub_.Mouse()



timepuly = 0
timemob = 0

score = 0

def start():
    start_button.Hide()
    score_board.Show()
    
    global run_poly
    run_poly = False


    




start_button = py2D.Widgets_.Buttons(
    win.screen,
    [125,100],[200,60],
    'Start',(0,0,0),45,45,
    (20,100,230),(10,70,120),(30,120,220),
    10,
    start
)

score_board = py2D.Widgets_.TextBoxs(
    win.screen,
    [5,5],[80,20],
    18,(0,100,0),
    (0,100,0),
    lambda:print(''),
    2,2
)

f_score_board = py2D.Widgets_.TextBoxs(
    win.screen,
    [125,200],[200,50],
    40,(0,100,0),
    (0,100,0),
    lambda:print(''),
    2,2
)



f_score_board.Hide()
score_board.Hide()
f_score_board.Set_output_disable()
score_board.Set_output_disable()




class Shatl:
    def __init__(self):
        self.pos = [225,580]
        self.size = [15,20]
        #self.shatl = win.Shape2D.Rect(
        #    'red',self.pos,self.size,0,win.screen
        #)


    def Update(self):
        global timepuly
        global timemob
        global bgx , bgy

        
        
        self.pos[0] = mous.Get_Pos()[0]
        bgx= mous.Get_Pos()[0]
        bgy= mous.Get_Pos()[1]
        
        self.shatl = win.Shape2D.Rect(
            (20,100,200),self.pos,self.size,0,win.screen
        )
        self.fly = win.Shape2D.Rect(
            (20,100,200),[self.pos[0]-7,self.pos[1]+3],[30,5],0,win.screen
        )
        corabl.Draw([self.pos[0],self.pos[1]-25])
        

        timepuly += 1
        timemob += 1
        if timepuly%17==0:
            pos = [self.shatl.up[0]+23,self.shatl.center[1]-22]
            bulet.added_bulet(pos)

        if timemob%17==0:
            mobpos = [random.randint(70,win.width-70),-100]
            hp = random.randint(1,4)
            mobpos = [mobpos,hp]
            mobici.add_mob(mobpos)
       
bulets = py2D.Objectes_('bulets')
class Bolet:
    def __init__(self,sped):
        global bulets
        self.sped = sped


    def added_bulet(self,pos):
        bulets.Add(pos,True)
    def Update(self):
        
        bul = bulets.Get_pack()
        
        for i in range(len(bul)):
            if bul[i-1][1]<0:
                    bulets.Del_min(i-1)

        for i in range(len(bul)): 
            buly.Draw([bul[i][0]-25,bul[i][1]-33])
            
            bul[i][1]-=self.sped


mobs = py2D.Objectes_('mobs')
class Mobs:
    def __init__(self):
        global mobs,score
        self.spedmob = 2
        
    def add_mob(self,pos):
        mobs.Add(pos,True)

    def Update(self):
        global score,run
        mob = mobs.Get_pack()
        bul = bulets.Get_pack()
        for i in range(len(bul)):
            for j in range(len(mob)):
                
                if bul[i][0]>mob[j-1][0][0]-20 and bul[i][0]<mob[j-1][0][0]+20 and bul[i][1]<mob[j-1][0][1]+20 and bul[i][1]>mob[j-1][0][1]-20:
                        
                            mobs.Del_min(j-1)
                            
                            score+=1
                        
                            
                            bax1.Draw([bul[i][0]-20,bul[i][1]-20])
                            
                            bax2.Draw([bul[i][0]-20,bul[i][1]-20])
                            
                            bax3.Draw([bul[i][0]-20,bul[i][1]-20])
                                
                    
                    
                            score_board.Set_text(score)


        for i in range(len(mob)):
            if mob[i-1][0][1]>win.height:
                    mobs.Del_min(i-1)
                    run = False

        for i in range(len(mob)):
            
            if mob[i][1]==2:
                ploxysh_2.Draw([mob[i][0][0]-20,mob[i][0][1]-20])
            elif mob[i][1]==1:
                ploxysh_1.Draw([mob[i][0][0]-20,mob[i][0][1]-20])

            
            
            if mob[i][1]==1:
                self.spedmob=2
            elif mob[i][1]==2:
                self.spedmob=8
            else:
                self.spedmob=2
            mob[i][0][1]+=self.spedmob
        return run
        









while (run_poly):
    run = win.close() ; win.set_fps(120) ; win.Update().BG_col('black')

    start_button.Update()




kadr = 0

mobici = Mobs()
bulet = Bolet(4)
boing = Shatl()
while (run):
    run = win.close() ; win.set_fps(60) ; win.Update().BG_col('black')
    bg.Draw([100-bgx,0])

    boing.Update()
    bulet.Update()
    run = mobici.Update()
    score_board.Update()

score_board.Hide()
f_score_board.Show()
while (run1):
    run1 = win.close() ; win.set_fps(60) ; win.Update().BG_col('red')

    f_score_board.Update()
    
    f_score_board.Set_text(score)



    