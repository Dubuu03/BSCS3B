haystack="sssssssadbutsad"
needle="sad"

i=0

if needle in haystack:
    while i < len(haystack):
        if haystack[i:i+len(needle)] == needle:
            break
        i+=1
    
print(i)