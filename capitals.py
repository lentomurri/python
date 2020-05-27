import random, json

with open (r"C:\Users\Lento\personalBatches\capitals.json", "r") as capitals:
    data = json.load(capitals)
    capitals.close()

def createQuiz():
# create a random list of answer, to choose the three random wrong ones for the quiz and the mixed questions
    shortName = list(data)
# create a loop to generate the file a fixed number of times 
    for i in range(1):
    # mix the answers everytime so the questions will be different
        random.shuffle(shortName)
        # for each state we create question and available options
        for state in shortName:
            # create an array with the right answer and three wrong ones
            answers = []
            #append right answer
            answers.append(data[state]["capital"])
            #append three wrong ones
            number = 0
            while number < 3:
                choice = data[shortName[random.randint(0, len(shortName) - 1)]]["capital"]
                # if choice is the same as the correct answer already, number goes back and it tries again
                if choice in answers:
                    number -= 1
                    pass
                answers.append(choice)
                number += 1
            # shuffle 
            random.shuffle(answers)
            #create file with right answers
            fileAnswer = open(r"C:\Users\Lento\Desktop\SelfTaught\tstp\python\TEST\answer" + str(i) + ".txt", "a")
            fileAnswer.write(str(answers.index(data[state]["capital"]) + 1) + "  " + data[state]["capital"] + "\n")
            fileAnswer.close()
            # create file with number variable according to test
            fileQuiz = open(r"C:\Users\Lento\Desktop\SelfTaught\tstp\python\TEST\file" + str(i) + ".txt", "a")
            # create question
            question = "What is the capital of " + str(data[state]["name"]) + "?\n"
            # append question
            fileQuiz.write(question)
            # append the available options as numbered strings
            for index, name in enumerate(answers):
                option = str(index + 1) + "): " + name + "\n"
                fileQuiz.write(option)
            fileQuiz.close()

createQuiz()
