def format_phone_numbers(N, phone_numbers):
    formatted_numbers = []
    
    for number in phone_numbers:
        if number.startswith('8'):
            number = '+7' + number[1:]
        elif number.startswith('9'):
            number = '+7' + number
        
        formatted_number = '+7 (' + number[2:5] + ') ' + number[5:8] + '-' + number[8:10] + '-' + number[10:]
        formatted_numbers.append(formatted_number)
    
    return formatted_numbers