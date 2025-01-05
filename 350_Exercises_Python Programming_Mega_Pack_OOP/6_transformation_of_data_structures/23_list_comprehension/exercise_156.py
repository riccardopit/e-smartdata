'''
The gaming.txt file is attached to this exercise. This file has been loaded into the text variable.
From the text list delete all newline characters. Then delete empty lines and print the text to the console.
Expected result:
[
    'Activision Blizzard',

    'Activision Blizzard, Inc. is a developer and publisher of interactive entertainment content and services.
    The Company develops and distributes content and services across various gaming platforms,',

    'including video game consoles, personal computers (PC) and mobile devices.
    Its segments include Activision Publishing, Inc. (Activision), Blizzard Entertainment, Inc. (Blizzard),',

    'King Digital Entertainment (King) and Other. Activision is a developer and publisher
    of interactive software products and content. Blizzard is engaged in developing and publishing of interactive',

    'software products and entertainment content, particularly in PC gaming. King is a mobile entertainment company.
    It is engaged in other businesses, including The Major League Gaming (MLG) business;',

    'The Activision Blizzard Studios (Studios) business, and The Activision Blizzard Distribution (Distribution)
    business. It also develops products spanning other genres, including action/adventure,',

    'role-playing and simulation.']
'''

import os.path

file_name = 'gaming.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)
with open(file_path, 'r') as file:
    text = file.readlines()
text = [x.replace('\n', '') for x in text]
text = [x for x in text if len(x) > 0]
print(text)
