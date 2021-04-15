import time;
#########################
fileToOpen = "list1.txt";
#########################

class READ():
    
    def __init__(self, file, speed):
        self.file = file;
        self.speed = 60/speed; #min/word
        self.countfile = 0
        #open the file
        file = open(fileToOpen,"r");
        
        self.text = file.readlines();
        #close
        file.close();
    
    def corrigirText(self):
        #esta funcao serve para corrigir as palavras
        a=[];
        for each in self.text:
            a.append(each.replace("\n",""))
        
        self.text=a;
        
    def count(self):
        counter = 0;
        for each in self.text:
            counter+=1
        
        self.countfile = counter;
        
    def list1(self):
        #print one list of word
        for i in range(0,1):
            for each in self.text:
                print("\t"+"\t"+"\t"+each)
                time.sleep(self.speed)
                
    def list2(self):
        #print two lists of word
        for i in range(len(self.text)):
            #jump 2
            if (i%2==0):
                try:
                    #even list
                    print(str(i)+"\t"+"\t"+self.text[i]+"\t"+"\t"+self.text[i+1])
                except:
                    #odd list
                    print(str(i)+"\t"+"\t"+self.text[i])
                
                time.sleep(self.speed)
        
    def ziguezague(self):
        for i in range(len(self.text)):
            #jump 2
            if (i%2==0):
                try:
                    #even list
                    print(str(i)+" "+self.text[i]+"\t"+"\t"+"\t"+"\t"+self.text[i+1])
                except:
                    #odd list
                    print(str(i)+"\t"+"\t"+self.text[i])
                
                time.sleep(self.speed)
        
    def book(self):
        pass;


#call the main function
book = READ(fileToOpen, 120);

#print(book.file)
#print(book.speed)
#print(book.text)
book.corrigirText()
#print(book.text)
book.count()

print(book.countfile)
print(book.speed)
print(time.clock())
#book.list1()
#book.list2()
#book.ziguezague()
print(time.clock())
