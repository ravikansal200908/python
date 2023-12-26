'''
- It just like a dictionary that contian varialbe and it's value
- namespace ansure that one time one variable tag one value/object at a time.
- types of namespaces
    - built-in namespace
        - dir()
    - module level/global namespace
        - it created for a each module
        - because of that two module can contain same variable/function etc.
    - local namespace
    - enclosed namespace
'''

a = 20
print(id(a))
print(id(20))
