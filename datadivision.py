import xml.etree.cElementTree as ET
from filedetect import list

tree = ET.ElementTree(file='test5.xml')
root = tree.getroot()
countPredatory = 0
countNonPredatory = 0
totalConvCount = 0
convid = []

for conversation in root:
    if conversation.tag == 'conversation':
        print(conversation.attrib['id'])
        converdsationId = conversation.attrib['id']
        totalConvCount += 1
        for author in conversation.iter('author'):
            convid.append(author.text)
        check = any(item in convid for item in list)
        if check:
            predatorylaceholder = open(
                'cleanedData/predatory/'+conversation.get('id')+'.txt', 'w')
            for attr in conversation.iter('text'):
                print('****reahced the place found predatory****')
                predatorylaceholder.write(attr.text)
            countPredatory += 1
        else:
            nonpredatorylaceholder = open(
                'cleanedData/nonpredatory/'+conversation.get('id')+'.txt', 'w')
            for attr in conversation.iter('text'):
                print('not predatory')
                nonpredatorylaceholder.write(attr.text)
            countNonPredatory += 1
        convid.clear()
