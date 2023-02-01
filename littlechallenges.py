# palindrome words

# def palindrome(sentence):
#     for i in (",. '?/><}{{}}'"):
#         sentence = sentence.replace(i, "")
#     palindrome = []
#     words = sentence.split( ' ')
#     for word in words:
#         word = word.lower()
#         if word == word[::-1]:
#             palindrome.append(word)
#     return palindrome
# sentence = input("Enter a sentence: ")
# print(palindrome(sentence))

#text to hand writing using python
# import pywhatkit as kit
# import cv2

# Handwritten = input("Enter your text to convert to handwritten: ")
# kit.text_to_handwriting(Handwritten, save_to="pythoncoding.png")
# img = cv2.imread('pythoncoding.png')
# cv2.imshow("python coding", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#graphs
import plotly.graph_objects as go

fig = go.Figure(go.Treemap(
    labels = ["A","B","C","D","E","F","G","H","I"],
    parents = ["","A","A","C","C","A","A","G","A"]
))
fig.show()

