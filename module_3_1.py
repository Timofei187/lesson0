calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    result = (len(string), string.upper(), string.lower())
    count_calls()
    return result

def is_contains(string, my_list):
    count_calls()
    for s in my_list:
        if string.lower() == s.lower():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
