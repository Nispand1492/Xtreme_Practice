import sys
import fileinput

def chk_for_palin():
        d = {}
        s = input()
        s = str(s).strip("\n")
        l = list(s)
        for x in l:
            if x not in d:
                d[x] = 1
            else :
                d[x] = d[x]+1
                
        if len(s)%2==0:
            for x in d:
                if d[x]%2!=0:
                    ans = "NO"
                    break
                else:
                    ans = "YES"

        else:
            cntr = 0
            for x in d:
                if d[x]%2!=0:
                    cntr=cntr+1
            if cntr !=1:
                ans = "NO"
            else :
                ans = "YES"
        return ans
        


if __name__ == '__main__':
    sys.stdout.write(chk_for_palin())