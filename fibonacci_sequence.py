# Fibonacci

print('Fibonacci Sequence')

terms = int(input('Number of terms:'))

term_1 = 0
term_2 = 1
counter = 3

print(f'''
{term_1}
{term_2}''')

while counter <= terms:
	
	next_term = term_1 + term_2
	print(next_term)
	term_1 = term_2
	term_2 = next_term
	counter+=1
	
print('End')