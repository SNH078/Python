# 1 --- MATCH STATUS :
# like "switch"

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "NOT FOUND"
        case 500:
            return "Internal server error"
        case _:
            return "Unknown status"

print(http_status(540))

#  2 -- DICTIONARY MERGE & UPDATE operators
dict1={'a':1 ,'b':2}
dict2={'b':3,'c':4}
merged=dict1|dict2
print(merged)



