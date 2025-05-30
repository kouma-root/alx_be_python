story = "On a beautiful {0} day, I went to the zoo. I saw a funny {1} monkey swinging from the trees. Then, I spotted a majestic {2} lion lounging in the sun. What a wild and {3} experience!"
adjective1 = input("Enter the first adjective: ")
adjective2 = input("Enter the second adjective: ")
adjective3 = input("Enter the third adjective: ")
adjective4 = input("Enter the fourth adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")

completed_story = story.format(adjective1, adjective2, adjective3, adjective4)

print(completed_story)