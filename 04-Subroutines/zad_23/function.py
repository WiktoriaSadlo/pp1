def letter_e(n):
    sum = 0
    for x in range(len(n)):
        if n[x]=='e' or n[x]=='E':
            sum+=1
    return sum

if __name__=="__main__":
    print(letter_e("Ewa ma dwa eklerki"))