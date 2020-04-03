# importing csv module 
import csv 

# initializing the titles and rows list 
allTeamAnswers = []
answerKey = []
outputFileName = "defaultOutput.txt"

def main():
	ReadCsvs()
	scores = {}
	for teamAnswers in allTeamAnswers: 
		# parsing each column of a teamAnswers
		scores[teamAnswers[1]] = CheckAnswers(teamAnswers[1], teamAnswers[2:len(teamAnswers)])
	for key in scores:
		results = key + '->' + str(scores[key])
		print results
		# writeToFile(results)

def ReadCsvs():
	global answerKey
	global allTeamAnswers
	global outputFileName
	# answerKeyFile = input("Enter Answer Key File Path: ")
	# teamAnswerFiles = input("Enter Teams' Answers File Path: ")
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
	perAnswerInfo = []
	perTeamInfo = []
	perAnswerInfo.append(["Team Name", "Question Score", "Team Answer", "Official Answer"])
	perTeamInfo.append(["Team Name", "Total Score"])

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
		helpfulInfo.append("%s\t%s\t\t%s" % (str(answerScore), teamAnswers[i], answerKey[i]))
		perAnswerInfo.append([teamName, str(answerScore), teamAnswers[i], answerKey[i]])
	headline = "\n%s (%s)\nScore\tTeam Answer\tOfficial Answer" % (teamName, score)
	helpfulInfo.insert(0, headline)
	perTeamInfo.append(teamName, str(score))
	PrintAnswers(helpfulInfo)

	# writeToFile(helpfulInfo)
	return score

def PrintAnswers(answers):
	for col in answers: 
		print("%s"%col)

def initializeOutputFile():
	outputFile = open(outputFileName, "w")
	outputFile.write("Result Output File\n")
	outputFile.close()

def writeToFile(output):
	# TODO::Convert list to string
	outputFile = open(outputFileName, "a")
	outputFile.write(output)
	outputFile.close()

if __name__ == "__main__":
    main()


