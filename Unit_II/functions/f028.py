def legends(func):
    def checkker(name):
        if name == 'Mountbatten':
            print('Mountbatten Was not an indian legend')
        else:
            func(name)
    return checkker


@legends
def indian_legends(name):
    print(name, 'Was a indian legend')


indian_legends('Swami Vivekanand')
indian_legends('Mahatma Gandhi')
indian_legends('Mountbatten')
indian_legends('Aarya Bhatt')
