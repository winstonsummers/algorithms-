# # if a given closure is greater than its opener then this is False
# # if in the end the total closures and total openers are not equal this is false.
# # if next closure is not equal to the previous opener this is false
# def test_brackets(s):
#   brackets = {
#     "{":0,
#     "}":0,
#     "[":0,
#     "]":0,
#     "(":0,
#     ")":0,
#     "openBrackets":[]
#   }
#   while(len(s)):
#     try:
#       brackets[s[0]] += 1
#       # Check that there are not more closures than openers 
#       if brackets.get("{") < brackets.get("}") or brackets.get("[") < brackets.get("]") or brackets.get("(") < brackets.get(")"):
#         #False string. More closures than openers
#         return False
#       #Checking for opener
#       elif(s[0] == "[" or s[0] == "(" or s[0] == "{"):
#         #add to openBrackets
#         brackets["openBrackets"].append(s[0])
#       #Check if closure is equal to the last opener
#       elif(s[0] == ")" and brackets.get("openBrackets")[-1] == "(" or s[0] == "]" and brackets.get("openBrackets")[-1] == "[" or s[0] == "}" and brackets.get("openBrackets")[-1] == "{"):
#         #Remove last openBracket from array
#         brackets["openBrackets"]=brackets["openBrackets"][:-1]
#       else:
#         return False
#     except:
#       pass
#     s=s[1:]
#   #Checking that all openers are equal to all closures
#   if brackets.get("[") + brackets.get("(") + brackets.get("{") != brackets.get("}") + brackets.get("]") + brackets.get(")"):
#     return False
#   return True

# print(test_brackets('abc(123)'))
# #returns true

# print(test_brackets('abc(123'))
# #returns false -- missing closing bracket

# print(test_brackets('a[bc(123)]'))
# #returns true

# print(test_brackets('a[bc(12]3)'))
# #returns false -- inproperly nested

# print(test_brackets('a{b}{c(1[2]3)}'))
# #returns true

# print(test_brackets('a{b}{c(1}[2]3)'))
# #returns false -- inproperly nested

# print(test_brackets('()'))
# #returns true

# print(test_brackets('[]]'))
# #returns false - no opening bracket to correspond with last character

# print(test_brackets('abc123yay'))
# #returns true -- no brackets = correctly matched




# Open [""]
# Close [""]
# #"[]([])" will return true
# #([)] will return false
# #{}{(}[]) will return false
# #{{}{()}[]} should return true
def test_brackets(s):
  brackets = {
    "{":0,
    "}":0,
    "[":0,
    "]":0,
    "(":0,
    ")":0,
  }
  while(len(s)):
    #Try adding last item
    try:
      brackets[s[-1]] += 1
    except:
      pass
    #Try adding first item
    try:
      brackets[s[0]] += 1
      print(brackets["{"])
      #Check for matching closure each time a opener is found
      if((brackets.get("{")) and (brackets.get("}")) and (brackets.get("{")>=brackets.get("}"))):
        brackets["{"] -=1
        brackets["}"] -=1
      elif((brackets.get("[")) and (brackets.get("]")) and (brackets.get("[")>=brackets.get("]"))):
        brackets["["] -=1
        brackets["]"] -=1
      elif((brackets.get("(")) and (brackets.get(")")) and (brackets.get("(")>=brackets.get(")"))):
        brackets["("] -=1
        brackets[")"] -=1
      elif(len(s)<=2):
        return False
    except:
      pass
    s=s[1:]
    s=s[:-1]
  return True
print(test_brackets("[{][}]]"))
