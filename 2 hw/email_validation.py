def fun(s):
    parts = s.split('@')
    if len(parts) != 2:
        return False
    
    username = parts[0]
    website_extension = parts[1].split('.')
    
    if len(website_extension) != 2:
        return False
    
    website = website_extension[0]
    extension = website_extension[1]
    
    valid_chars = set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_')
    
    if not all(char in valid_chars for char in username):
        return False
    
    if not all(char in valid_chars for char in website):
        return False
    
    if not all(char.isalpha() for char in extension) or len(extension) > 3:
        return False
    
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
