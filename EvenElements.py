import  random;

def elements():
    a = random.sample(range(1,30),10)
    print(a);
    print("Even numbers are: ")
    for i in a:
        if (i%2==0):
            print i;
        #print ("New List", +a);

elements()
