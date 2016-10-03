import nltk
import os
def my_fun(str):
	line = str
	line = line.replace(" and "," ")
	line = line.replace(" is "," ")
	line = line.replace(" of "," ")
	line = line.replace(" in "," ")
	line = line.replace(" are "," ")
	line = line.replace(" to "," ")
	line = line.replace(" a "," ")
	line = line.replace(" the "," ")
	line = line.replace(" both "," ")
	line = line.replace(" be "," ")
	return line


#Initialize the training data (restaurants and labels)
train = []
label = []
#Operating the file and training data
file = open("computer.txt")
i = 0
while 1:
	line = file.readline()
	line = my_fun(line)
	if not line:
		break
	else:
		train.append(nltk.word_tokenize(line))
		label.append('C')
file.close()

file = open("music.txt")
while 1:
	line = file.readline()
	line = my_fun(line)

	if not line:
		break
	else:
		train.append(nltk.word_tokenize(line))
		label.append('M')
file.close()

file = open("biology.txt")
while 1:
	line = file.readline()
	line = my_fun(line)

	if not line:
		break
	else:
		train.append(nltk.word_tokenize(line))
		label.append('B')
file.close()


#Self-define function, which returns the frequency distribution of restaurant words in documents
def document_features(documents): 
    fdist = nltk.FreqDist(documents)
    return fdist

#documents = training data + label, print them to see the contents
documents = []
for a in range(0,len(train)) :
	documents.append((train[a],label[a]))

#feature = frequency distribution of restaurant words in documents + label
doc_feat = []
for a in range(0,len(train)) :
	doc_feat.append((document_features(documents[a][0]),documents[a][1]))
		
#To train the Naive Bayes classifier using training data, print the training data accuracy
classifier = nltk.NaiveBayesClassifier.train(doc_feat)
acc_1 = nltk.classify.accuracy(classifier, doc_feat)
print "classifier's accuracy on training data:%f"%(acc_1)


#To classify a new testing data using the newly-trained classifier (get a label)
test = []
Result_Label = []
file = open("test.txt")
i = 0
while 1:
	line = file.readline()
	
	if not line:
		break
	else:
		test.append(nltk.word_tokenize(line))
		Result_Label.append(classifier.classify(document_features(test[i])))
	i = i+1
file.close()

file = open("result.txt","w")
for a in range(0,len(test)):
	for i in range(0,len(test[a])):
		file.write(test[a][i])
		file.write(' ')
	file.write(Result_Label[a])
	file.write('\n')
file.close()


documents_2 = []
for a in range(0,len(test)) :
	documents_2.append((test[a],Result_Label[a]))
#feature = frequency distribution of restaurant words in documents + label
doc_feat_2 = []
for a in range(0,len(test)) :
	doc_feat_2.append((document_features(documents_2[a][0]),documents_2[a][1]))
		
#To train the Naive Bayes classifier using training data, print the training data accuracy
acc_2 = nltk.classify.accuracy(classifier, doc_feat_2)

print "classifier's accuracy on test data:%f"%(acc_2)