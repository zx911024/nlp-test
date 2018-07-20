# coding=UTF-8
import main
import processBar
import fileTools

filePathNames=fileTools.eachFile("./resourcesTest/")
#print(filePathNames)
maxAllstep=len(filePathNames)
process_bar1 = processBar.ShowProcess(maxAllstep)
trainData= open("trainData",'w')
for path in filePathNames:
    process_bar1.show_process()
    fileNames=fileTools.eachFile(path+"/")
    #maxstep = len(fileNames)
    #process_bar = processBar.ShowProcess(maxstep)
    for item in fileNames:
        #process_bar.show_process()
        content=fileTools.readFile(item)
        #print(content)
        segmemtSentence=main.evaluate_line(content)
        print(segmemtSentence)
        exit()
        number=0
        for num in segmemtSentence:
            tag=num.split("/")
            if tag[1] in ["nr","nrf","nrj"]:
                number+=1
        if number:
            for word in segmemtSentence:
                ll=word.split("/")
                #print(ll[0][0])

                if ll[1] not in ["nr","nrf","nrj"]:
                    for i in ll[0]:
                        a = "".join([i," ","O", "\n"])
                        try:
                            trainData.write(a)
                        except Exception as e:
                            trainData.write(repr("".join([i," ","O", "\n"])))
                        # trainData.write(i +" "+"O"+"\n")
                        #print(i+" "+"O")
                else:
                    for j,ii in enumerate(ll[0]):
                        if j==0:
                            a= "".join(([ii," ","B-PER","\n"]))
                            try:
                                trainData.write(a)
                            except Exception as e :
                                trainData.write(repr("".join([ii, " ", "B-PER", "\n"])))
                            #print(ii+" "+"B-PER")
                        else:
                            a= "".join([ii, " ", "I-PER", "\n"])
                            try:
                                trainData.write(a)
                            except Exception as e:
                                trainData.write(repr("".join([ii, " ", "I-PER", "\n"])))
                            #print(ii+" "+"I-PER")
            number=0
        else:
            continue
    #process_bar.close()
trainData.close()




