print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

combine_names = name1 + name2
lower_names = combine_names.lower()
t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')
first_digit = t + r + u + e

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')
second_digit = l + o + v + e

love_scores = int(str(first_digit) + str(second_digit))

if love_scores < 10 or love_scores > 90:
    print(f'Your score is {love_scores}, you go together like coke and mentos.')
elif 40 <= love_scores <= 50:
    print(f'Your score is {love_scores}, you are alright together')
else:
    print(f'Your score is {love_scores}')









