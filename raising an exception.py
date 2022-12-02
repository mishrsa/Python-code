#from webbrowser import get


#def get_ratios(l1, l2):
    ratios = []
    for i in range(len(l1)):
        try:
            ratios.append(l1[i]/float(l2[i]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('get ratios called with bad args')
    return ratios


l1 = [1,2,3,4]
l2 = [5,6,7,0]
#print(get_ratios(l1,l2))

def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")

print(fancy_divide([0, 2, 4], 1))