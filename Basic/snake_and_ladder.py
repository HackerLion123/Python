import random


class Board:
	def __init__(self,length,breadth):
		board = [[" "]*length]*breadth

	def random_snakes(self):
		for i in range(0,5):

	def display(self):
		print("---------------------------------------------------------------------------------------------------------------------------------------");
		for each in board:
			for e in each:
				print("|"+e,end=" ")
			print()


class Player:
	"""players in the game"""
	def __init__(self, name,gamesPlayed = 0,wins = 0):
		self._name = name
		self._gamesPlayed = gamesPlayed
		self._wins = wins

	@property
	def name(self):
		return self._name

	@property
	def gamesPlayed(self):
		return self._gamesPlayed
	
	
		
def main():

	print("""                     :/o:ss:.                                                                                                                 
	                .+ss+hs+yyyy/                                                                                                               
	            ``.sysssssssssssh:                                                                                                              
	     `-/oyhhyyyysssyyysssssyh`                                      -/:                                                                     
	  `/syysyyyyssyysssyhyyssyhs-`                                     -hyy`                                                                    
	 +yysssyyyyso/:/osyyyyyso:..`/.                                    :hyy.                                                                    
	oyssssyhy+.      ``````                                            :hyh-                                         `:////.                    
	dsssssys`                                                          :yyh.                                        /o-````:s.                  
	ohyyssyy/.                                                         :hyh.                                       :s.+/:o`s.h                  
	 +hhysssyyyso/:.`                       ``                         /hyy    `-:::-                              :o :.:/o+.h                  
	  .+syysssssyhhhyso/:-.               `/+++.           `-/+/       +hyy:/oyyyyyyo     `.--.`                    o+.   `-s:                  
	    `./osyyysyyyssoossyys+:.`    `-` -++++os        ./oyyyyy-     `oyyyyhyso+:-`    -/+++++/:       .:+ossso`    ./+//+:`                   
	        ``-:+ossyy+++sssss++oy+-.oo+/++/:+++.     :oyys+yyyyo    +yyyhh/.``        `+++:`./++/    `+yyyysoo/`                               
	               ``-+++syyyo+++hhhy++++ss. +++:   .oyys:`/yyyyy`   +yyyyhs+:-`       `+++.  :+++`   +yyys:.`                                  
	                 `+++.`-/++++yyys++++s.  :++o  -yyy+``+yysyyy/    .hhyyyyhyyo/-`   `+++/-:++/-    :++oyyyso+/:.`                            
	    -+y+          +++.   /+++sssys++/`   .++y-`yyyo`-syy/`oyyy-   `hhyo.-/+syhyys/-`:+++++-.`   .:++-.:/+osyyyys+`                          
	  -syh-           +++/:::+++osssyy++.     /++/:yyyysyyo.  `syyy:  `hhh+   :oo:+syyhy`./+++:...-/++/.+o/-..-/syyyy/                          
	 /yyyy.`          ++o/:oyo++ossyo++-      .+++.oyyyso:`    `oyyy/ `yyhs   syy: ``--:+o+-:/+++++/:-`.yyyyyyyyyyys+`                          
	 dsssyyssoo++/+++oyyyyyyy+++oys+.``        .:-` `..`        `:oo/  syy/   yyy/     shyy- `.....`    .-://++/:-.`                            
	 oysssssyyhyyyyyssyyysyyy+++/.`            .-----.                 ./-   `yyy/     oyyy:                                                    
	  :osyyyyyyyyyyyyyhhhs/::+++:             :yyyyy+`                       `yyy/     /yyy:                                                    
	    `.--:::/:::--.+++:```/++:             +yyyys                         `yyy/     :yyh/                                                    
	                  /++/:::+++:             .yyyyo                         .yyy/     :yyh+                                                    
	                  /++:   /++:            .:syyyy` .                      .yyy:     -yyy/                                           ```.```  
	                  /++/:::+++:           :yyysyyy+/y-                     .yyy:     .yyy+                                          `--/+---` 
	                  :++:```/++:           syyy.:yyyy/`     `.--`           .yyy:     `hyy+    ``..`               ``..                :/--.`  
	                  :++/.../++/           -syysssoss:   `-/osyy/           `yyy:      syy+  .+ossss+.     ```   ./osss:-/+++:         .+...+. 
	                  :++/:::/++/            `.---` ``` -+ssooyyys         `.-yyy/   ``.syys  syy+-/sys-   .oso``/syyoossyssoo+`        .+...+. 
	                  :++/   -+++                ``   `+sso-.oyyyy-     `-/osyyyys`./osyyyyh- syy-  oyy+   .yyy+syys/`syys/-``         -..+++:.`
	                  :++/:::/.+++`        ``.-::////-.oys: .oyssyyo    -oss+/syyyysyso/oyyyys`oyyo/+sso.   .syyyyys.  :ossyso++:-.`    `` ````-+
	                  :++/   `+++.    `.-:/+++//:--..oyy+`:ss+`.syy: `+ys+.`+yysyyys-`:syssyy+:syyys:.   `/ssyyyys.     .-:/+ossyso/    .:  `  `
	                  -++/:::/+++-`-:/+++//:.``     .syyssys:   :sys/oyys:/oysooyyys/oyso--syy+-+syso:::+sso-syyy:     :o+:-.-/syyys` ``+:-/:+  
	                  -++/    :+++++++/:.`           :oso+:`     :syysssssso/- :ssssss+-`  -oss- ./osssss+-` /sss`     :ssssssssso+- `/:`..`:/  
	                  `:./    `-:::-.`                            `:/-....`     .--.`        ``     `..``     .-.       `..----.`    `++:`      
	                                                                                                                              .` :: `/+-    
	                                                                                                                              --:-+-.::     
	                                                                                                                           .-`o..//--.      
	                                                                                                                           `/+/::/--        
	                                                                                                                       `.:`  .+-            
	                                                                                          """)


	players = input("Enter the number of players ")

	board = Board(16,16)

	
if __name__ == '__main__':
	main()