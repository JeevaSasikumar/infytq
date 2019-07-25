#PF-Prac-5
def count_digits_letters(sentence):
    #start writing your code here
    result_list=[]
    c=0
    d=0
    for i in range(0,len(sentence)):
        if(sentence[i]>="A" and sentence[i]<="Z"):
            c+=1
        if(sentence[i]>="a" and sentence[i]<="z"):
            c+=1
        if(sentence[i]>="0" and sentence[i]<="9"):
            d+=1
    result_list.append(c)
    result_list.append(d)
    
    return result_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))
