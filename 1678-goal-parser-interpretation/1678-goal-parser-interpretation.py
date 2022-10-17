class Solution:
    def interpret(self, command: str) -> str:
        i=0
        n=len(command)
        o=''
        while i<n:
            if command[i]=='G':
                o+='G'
                i+=1
            elif command[i]=='(' and command[i+1]==')':
                o+='o'
                i+=2
            else:
                o+='al'
                i+=4
        return o
        