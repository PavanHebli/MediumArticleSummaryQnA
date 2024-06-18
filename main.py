from helper import CheckMediumLink, FetchMediumLink, GenerateQuizQuestions, GetSummary
from constants import inputMessage
import argparse


# TODO:
# 1. Add Randomness to the answers.
# 2. Complete argument parser functionality to switch between summary and quiz.
# 3. Fix bug: sometimes the requests module returns None. (implement different agents)


# parser = argparse.ArgumentParser()
# parser.add_argument("-qna", dest = "type", action='store_true', default = False, help="Server name")
# # parser.add_argument("-host", "--hostname", dest = "hostname", default = "xyz.edu", help="Server name")
# args = parser.parse_args()

ipURL= input(f"enter medium URL here (e.g.- https://medium.com/xxxxxxxxxxxx): ")
responseBS = FetchMediumLink(ipURL)
if CheckMediumLink(responseBS):
    article = responseBS.find('article')
    inputText=""
    for paragraph in article:
        inputText+=paragraph.text+ " "
    summaryText=GetSummary(inputText)
    questionsGenerate=input(inputMessage.quizQuestions).strip()
    if questionsGenerate =="" or questionsGenerate== "q" or questionsGenerate == "quit":
        questionsGenerate=None
    else:
        questionsGenerate= int(questionsGenerate)
        if questionsGenerate <=inputMessage.quizQuestionsNone:
            questionsGenerate=None
        elif questionsGenerate > inputMessage.quizQuestionsNumber:
            questionsGenerate=inputMessage.quizQuestionsNumber
    if questionsGenerate:
        qList=[]
        aList=[]
        inCorctList=[]
        while len(qList) != questionsGenerate:
            summaryText=GenerateQuizQuestions(questionsGenerate, inputText)
            temp= summaryText.split("#")
            temp=temp[1:]
            for data in temp:
                data = data.split("\n")
                qList.append(data[0])
                aList.append(data[1])
                inCorctList.append(data[2])
        for question, right, wrong in zip(qList,aList,inCorctList):
            right=right.split(":")[1]
            wrong=wrong.split(":")[1]
            print(question)
            print(f"A: {right}")
            print(f"B: {wrong}")
            ansDict={"a":"Correct Answer!!", "b":"Wrong Answer :("}
            answr=input("type option A or B to answer and press enter (type Q/Quit to quit): ").strip().lower()
            if answr== "q" or answr == "quit":
                break
            answr=answr.strip().lower()
            print("-"*50)
            print(ansDict[answr])
            print("-"*50)

else:
    print(f"[Icorrenct URL] Not a Medium URL Icorrenct URL, please check the URL")

