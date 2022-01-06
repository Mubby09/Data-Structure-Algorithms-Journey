class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        current_path = ''
        
        for i in path + '/':
            if i == '/':
                if current_path == '..':
                    if stack: stack.pop()
                elif current_path != '' and current_path != '.':
                    stack.append(current_path)
                current_path = ''
                
            else:
                current_path += i
                
        return '/' + '/'.join(stack)
            