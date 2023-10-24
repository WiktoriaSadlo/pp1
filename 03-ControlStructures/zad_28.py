article_number = input('Enter EAN-13 article number:')

if len(article_number)==13 and article_number[:3]=='590':
    print('Article number is correct.')
    print('Article manufactured in Poland.')
elif len(article_number)==13:
    print('Article number is correct.')
else:
    print('Article number is incorrect.')