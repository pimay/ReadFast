# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 00:03:34 2021

@author: Pi
"""

import time;
#########################
fileToOpen = "pai_contra_mãe.txt".decode("utf-8");
#fileToOpen = "list1.txt";
#########################

class READ():
    
    def __init__(self, file, speed):
        self.file = file;
        self.speed = 60/speed; #seconds/word
        self.countLine = 0
        self.countWords = 0
        #open the file
        file = open(fileToOpen,"r");
        
        self.line = file.readlines();
        #close
        file.close();
    
    def corrigirText(self):
        #esta funcao serve para corrigir as palavras
        a=[];
        for each in self.line:
            a.append(each.replace("\n","").decode("utf-8"))
        self.line=a;
        
    def count(self):
        #count line
        countL = 0;
        countLM = 0;
        countW = 0;
        lm = [];
        for each in self.line:
            #count the number of lines
            countL+=1

            #old count Word is to make the difference between the counts
            oldCountW=countW;
            #count the number of words
            a=[];
            
            
            a.append(each.split(" "))
            for word in a[0]:
                countW += 1 if(word <> "") else 0

            #count the number of words per line and make the mean
            lm.append(countW-oldCountW)

        #make the mean per line
        sumLM =0
        for each in lm:
            sumLM+=each

        countLM = int(sumLM/len(lm))
            
            
        self.countLine = countL;
        self.countWord = countW;
        self.countLMean = countLM; #-need to be checked
        
        
    def list1(self):
        #print one list of word
        for i in range(0,1):
            for each in self.line:
                print("\t"+"\t"+"\t"+each)
                time.sleep(self.speed)
                
    def list2(self):
        #print two lists of word
        for i in range(len(self.line)):
            #jump 2
            if (i%2==0):
                try:
                    #even list
                    print(str(i)+"\t"+"\t"+self.line[i]+"\t"+"\t"+self.line[i+1])
                except:
                    #odd list
                    print(str(i)+"\t"+"\t"+self.line[i])
                
                time.sleep(self.speed)
        
    def ziguezague(self):
        for i in range(len(self.line)):
            #jump 2
            if (i%2==0):
                try:
                    #even list
                    print(str(i)+" "+self.line[i]+"\t"+"\t"+"\t"+"\t"+self.line[i+1])
                except:
                    #odd list
                    print(str(i)+"\t"+"\t"+self.line[i])
                
                time.sleep(self.speed)
        
    def book(self):
        #calculate how many words per time, depends of speed
        #calculate how many lines per time
        for each in self.line:
            print(each)
            time.sleep(self.speed);


#Open a file and close
book = READ(fileToOpen, 50);

#print(book.file)
#print(book.speed)
#print(book.text)
book.corrigirText()
#print(book.text)
book.count()

print("Number of line: " + str(book.countLine))
print("Number of word: " + str(book.countWord))
print("Number of word mean: " + str(book.countLMean))
print("Select Speed: " + str(book.speed*60) + " words/min")
print(time.clock())
#book.list1()
#book.list2()
#book.ziguezague()
book.book()
print(time.clock())
