#Thing 1
print("---Thing 1---")
mystery = '\U0001f4a9'
print(mystery)

#Thing 2
print('---Thing 2---')
pop_bytes = bytes(mystery.encode('UTF-8'))
print (pop_bytes)

#Thing 3
print('---Thing 3---')
pop_string = pop_bytes.decode('UTF-8')
print (pop_string)

#Thing 4
print('---Thing 4---')
poem = 'My kitty cat likes %s,\n' + \
    'My kitty cat likes %s,\n' + \
    'My kitty cat fell on his %s\n' + \
    'And now thinks he\'s a %s' 
print (poem % ('roast beef', 'ham', 'head', 'clam'))

#Thing 5
print('---Thing 5---')
letter = "Dear {salutation} {name},\n" + \
    "Thank you for your letter.  We are sorry that our {product} {verbed} in your \
{room}.  Please note that it should never be used in a {room}, especially near any {animals}.\n" + \
    "Send us your receipt and {amount} for shipping and handling.  We will send you another {product} \
{product} that, in our tests, is {percent}% less likely to have {verbed}.\n" + \
    "Thank you for you support.\n" + \
    "Sincerely,\n{spokesman}\n{job_title}"
print (letter)

#Thing 6
print('---Thing 6---')
fillDict = {'salutation': 'Captain', 'name': 'John', 'product': 'toaster', 'verbed':'exploded', 'room': 'bathroom',\
    'animals':'fish', 'amount': '$9.95', 'percent':'25', 'spokesman': 'Mr. Toaster', 'job_title': 'Toaster Explosion Specialist'}

print(letter.format(**fillDict))

#Thing 7
print ('---Thing 7---')
mammoth = "We have seen thee, queen of cheese,\n\
Lying quietly at your ease,\n\
Gently fanned by evening breeze,\n\
Thy fair form no flies dare seize.\n\
All gaily dressed soon you'll go\n\
To the great Provincial show,\n\
To be admired by many a beau\n\
In the city of Toronto.\n\
Cows numerous as a swarm of bees,\n\
Or as the leaves upon the trees,\n\
It did require to make thee please,\n\
And stand unrivalled, queen of cheese.\n\
May you not receive a scar as\n\
We have heard that Mr. Harris\n\
Intends to send you off as far as\n\
The great world's show at Paris.\n\
Of the youth beware of these,\n\
For some of them might rudely squeeze\n\
And bite your cheek, then songs or glees\n\
We could not sing, oh! queen of cheese.\n\
We'rt thou suspended from balloon,\n\
You'd cast a shade even at noon,\n\
Folks would think it was the moon\n\
About to fall and crush them soon."
print (mammoth)

#Thing 8
print('---Thing 8---')
import re
allStartCs = re.findall('\\bc\\w+\\b', mammoth)
print (allStartCs)

#Thing 9
print('---Thing 9---')
allFourLetterStartCs = re.findall('\\bc\\w{3}\\b', mammoth)
print(allFourLetterStartCs)

#Thing 10
print('---Thing 10---')
allEndRs = re.findall('\\w+r\\b', mammoth)
print (allEndRs)

#Thing 11
print('---Thing 11---')
allTripleVowels = re.findall('\\b\\w*[aeiou]{3}\\w*\\b', mammoth)
print(allTripleVowels)

#Thing 12
print('---Thing 12')
gifHex = '47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'
from binascii import unhexlify
gif = unhexlify(gifHex)
print (gif)

#Thing 13
print('---Thing 13---')
validGifHeader = b'GIF89a'
if (gif[:6] == validGifHeader) :
    print ('Valid GIF')
else:
    print ('Invalid GIF - more likely bad code')

#Thing 14
print('---Thing 14---')
import struct
width, height = struct.unpack('<HH', gif[6:10])

print("Height: {} Width: {}".format(height, width))