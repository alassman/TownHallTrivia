# importing csv module 
import csv, string

# Globals
allTeamAnswers = []
answerKey = []
answerPoints = []
outputTextFileName = ""
outputCsvFileName = ""
perAnswerInfo = []
perTeamInfo = []

def main():
    initializeGlobals()
    ReadCsvs()
    scores = {}
    for teamAnswers in allTeamAnswers: 
        scores[teamAnswers[1]] = CheckAnswers(teamAnswers[1], teamAnswers[2:len(teamAnswers)])
    writePerAnswerInfoToTextFile()
    writePerTeamInfoToCsv()

def ReadCsvs():
    global answerKey
    global answerPoints
    global allTeamAnswers
    global outputTextFileName
    global outputCsvFileName
    answerKeyFile = input("Answer Key File Name (use ""): ")
    teamAnswerFiles = input("Round Answers File Name (use ""): ")
    # answerKeyFile = "Round 1_AnswerKey.csv"
    # teamAnswerFiles = "Round 1.csv"
    outputTextFileName = teamAnswerFiles.split(".")[0] + "_DetailedResults.txt"
    outputCsvFileName = teamAnswerFiles.split(".")[0] + "_Results.csv"
    answerFields = []
    answerKeyFields = []
    with open(answerKeyFile, 'r') as csvfile: 
        answerKeyReader = csv.reader(csvfile)
        answerKeyFields = answerKeyReader.next() 
        answerKey = answerKeyReader.next()
        answerPoints = answerKeyReader.next()

    with open(teamAnswerFiles, 'r') as csvfile: 
        teamAnswersReader = csv.reader(csvfile)
        answerFields = teamAnswersReader.next()
        for row in teamAnswersReader: 
            allTeamAnswers.append(row)

def CompareCleansedAnswers(teamAnswer, officialAnswer):
    correct = 0
    for teamAnswerPart in teamAnswer:
        if teamAnswerPart in officialAnswer:
            correct += 1
            officialAnswer.remove(teamAnswerPart)
    return correct


def CheckAnswers(teamName, teamAnswers):
    global perAnswerInfo
    global perTeamInfo

    answerInfoInsertLocation = len(perAnswerInfo)
    score = 0
    for i in range(0, len(answerKey)):
        cleansedTeamAnswer = []
        cleansedOfficialAnswer = []
        # Get single answer as a list
        teamAnswer = teamAnswers[i].split(",")
        for teamAnswerPart in teamAnswer:
            # Cleanse all parts of answer of all white space
            cleansedTeamAnswer.append(cleanWord(teamAnswerPart))
        officialAnswer = answerKey[i].split(",")
        for officialAnswerPart in officialAnswer:
            cleansedOfficialAnswer.append(cleanWord(officialAnswerPart))
        answerScore = CompareCleansedAnswers(cleansedTeamAnswer, cleansedOfficialAnswer)
        score += answerScore
        if answerPoints[i] != str(answerScore):
            perAnswerInfo.append("%s\t%s\t%s\t%s\t|\t%s" % ("Question_" + str(i + 1), answerPoints[i], str(answerScore), teamAnswers[i], answerKey[i]))
    perAnswerInfo.insert(answerInfoInsertLocation, "\n%s (%s)" % (teamName, str(score)))
    perTeamInfo.append([teamName, str(score)])
    return score

# Removes punctuation, gets rid of whitespace, converts to lower case
def cleanWord(word):
    cleansedWord = word
    cleansedWord = cleansedWord.translate(None, string.punctuation)
    cleansedWord = "".join(cleansedWord.split())
    cleansedWord = cleansedWord.lower()
    return cleansedWord

def writePerAnswerInfoToTextFile():
    info = ""
    for line in perAnswerInfo:
        info = info + line + "\n"
    outputFile = open(outputTextFileName, "w")
    outputFile.write(info)
    outputFile.close()

def writePerTeamInfoToCsv():
    with open(outputCsvFileName, mode='w') as result_file:
        result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in perTeamInfo:
            result_writer.writerow(row)

def initializeGlobals():
    global outputTextFileName
    global outputCsvFileName
    global perAnswerInfo
    global perTeamInfo
    outputTextFileName = "defaultTextOutput.txt"
    outputCsvFileName = "defaultCsvOutput.csv"
    perAnswerInfo.append("---\nTeam_Name (Overall_Score)\nQuestion_X, Exp_Score, Act_Score, Team_Ans | Official_Ans\n---")
    perTeamInfo.append(["Team Name","Total Score"])

if __name__ == "__main__":
    main()


