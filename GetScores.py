# importing csv module 
import csv 

# initializing the titles and rows list 
allTeamAnswers = []
answerKey = []
outputFileName = "defaultOutput.txt"
perAnswerInfo = []
perTeamInfo = [["Team Name","Total Score"]]

def main():
	ReadCsvs()
	scores = {}
	for teamAnswers in allTeamAnswers: 
		scores[teamAnswers[1]] = CheckAnswers(teamAnswers[1], teamAnswers[2:len(teamAnswers)])
	writeToFile()


def ReadCsvs():
	global answerKey
	global allTeamAnswers
	global outputFileName
	answerKeyFile = "answerKey.csv"
	teamAnswerFiles = "Round 1.csv"
	outputFileName = teamAnswerFiles.split(".")[0] + "Results.txt"
	answerFields = []
	answerKeyFields = []
	with open(answerKeyFile, 'r') as csvfile: 
		answerKeyReader = csv.reader(csvfile)
		answerKeyFields = answerKeyReader.next() 
		answerKey = answerKeyReader.next()

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

	score = 0
	for i in range(0, 6):
		cleansedTeamAnswer = []
		cleansedOfficialAnswer = []
		# Get single answer as a list
		teamAnswer = teamAnswers[i].split(",")
		for teamAnswerPart in teamAnswer:
			# Cleanse all parts of answer of all white space
			cleansedTeamAnswer.append("".join(teamAnswerPart.split()))
		officialAnswer = answerKey[i].split(",")
		for officialAnswerPart in officialAnswer:
			cleansedOfficialAnswer.append("".join(officialAnswerPart.split()))
		# print "teamAnswers: ", teamAnswers[i], "officialAnswer: ", answerKey[i]
		# print cleansedTeamAnswer, "\t", cleansedOfficialAnswer
		answerScore = CompareCleansedAnswers(cleansedTeamAnswer, cleansedOfficialAnswer)
		score += answerScore
		perAnswerInfo.append("%s\t%s\t%s\t%s" % ("Question " + str(i)), str(answerScore), teamAnswers[i], answerKey[i])
	perAnswerInfo.insert("%s (%s)" % teamName, score, len(perAnswerInfo)-1)
	perTeamInfo.append([teamName, str(score)])
	return score

def initializeOutputFile():
	outputFile = open(outputFileName, "w")
	outputFile.write("Result Output File\n")
	outputFile.close()

def writeToTextFile(output):
	# TODO::Convert list to string
	outputFile = open(outputFileName, "a")
	outputFile.write(output)
	outputFile.close()

def writeToCsv(output):
    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['John Smith', 'Accounting', 'November'])

if __name__ == "__main__":
    main()


