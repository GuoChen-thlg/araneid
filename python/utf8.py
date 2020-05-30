def getUtf8(request):
    '''
     只处理requests返回的数据
     
    '''
    
    return request.text.encode(request.encoding).decode(
        'gbk').encode('utf-8').decode('utf-8')
