from string import Template 

class prompts:
    summary=Template("Write a short summary of 150-200 words of the following and start as the medium article talks about or medium article includes information on:\n $summaryVar")
    quizGenerator=Template("from the below infromation generate $questions flash card questions and two one-word answers for each question first being right second being wrong. differentiate answers as ans1 and ans2 and Start the question with 'Q:' and do not add numbers to the start of question. Start the response with this specfic line 'here are your questions'. Put # before the all the questions. keep the format simple without bold italic. \n here is the text:\n $summaryVar")

class inputMessage:
    quizQuestionsNone=0
    quizQuestionsNumber=6
    enterURL=f"enter Medium URL here (e.g.- https://medium.com/xxxxxxxxxxxx): "
    quizQuestions=f"want to test your knowledge? how many questions you would like to answer? (Max {quizQuestionsNumber}, type Q/Quit to quit): "
    answerQuestions="type option A or B to answer and press enter (type Q/Quit to quit): "
    incorrectURLMsg=f"[Incorrect URL] Not a Medium URL Icorrenct URL, please check the URL"

class ModelParam:
    model="llama3-8b-8192"
    api_key="XXXXXXXXXXXXXXXX" # Generate your own API Key from Groq: https://console.groq.com/keys
    temperature=1
    max_tokens=1024
    top_p=1
    stream=True
    stop=None