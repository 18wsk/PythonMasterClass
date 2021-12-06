# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='-', end=" ")
#     # this is evaluating arguments for the print function (sep, end)
#     # parameter = argument
#######################################################################
import webbrowser

# webbrowser.open("https://www.python.org/", new=2)
# # new doesnt apply for some browsers
# # says "if possible"
# help(webbrowser)

chrome = webbrowser.get(using='windows-default')
chrome.open_new_tab("https://www.python.org/")

#######################################################################
# register makes browsers available
