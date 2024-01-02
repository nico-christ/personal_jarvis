def is_string_in_array(target_string, string_array):
    for s in string_array:
        if s in target_string:
            return True
    return False

def find_string_in_array(target_string, string_array):
    for s in string_array:
        if s in target_string:
            return s
    return None

def is_string_in_array_multi(target_string, string_array, number):
    words = target_string.split()
    count = words.count(string_array)
    
    return count >= number