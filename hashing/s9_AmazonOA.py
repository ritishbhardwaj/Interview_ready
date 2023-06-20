'''problem statement link
https://leetcode.com/discuss/interview-question/3114099/AMAZON-OA-(INTERN-2024)
'''

from collections import Counter

def sol(s,t):
    c1=Counter(s)
    c2=Counter(t)
    steps=100000000000000
    for ch in t:
        steps=min(c1[ch]//c2[ch],steps)
    print(steps)

def main():
    sol("mononom","mon")
    sol("abacbc","bca")
    sol("abdadccacd","edac")

if __name__:
    main()
