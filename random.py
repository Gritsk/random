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
                print('*** found predatory****')
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

        
 !pip3 install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
 !pip install mxnet-cu110
  
