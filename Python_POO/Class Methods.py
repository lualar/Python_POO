import re
class watchEngraveError(Exception):
    def __init__(self, engrave, message):
        Exception.__init__(self, message)
        self.Engrave = engrave

class watch():
    __watches_created  = 0
    def __init__(self):
        watch.__watches_created += 1
        self.engraving = ''

    @classmethod
    def get_number_of_watches_created(cls):
        return '# of objects created: {}'.format(cls.__watches_created)

    @classmethod
    def including_brand(cls, sText):
        print('Class method was called')
        _watch = cls()
        _watch.engraving = sText
        return _watch

    @staticmethod
    def validateEngrave(sText):
        if (len(sText) > 40):
            raise watchEngraveError(sText, " Error. Engrave has more than 40 characters!")
        elif(re.match("^[a-zA-Z0-9]*$", sText) == None):
            raise watchEngraveError(sText, " Error. Engrave has a not alphanumeric engrave!")
        elif (' ' in sText):
            raise watchEngraveError(sText, " Error. Engrave has spaces!")
        return True
try:
    watch1 = watch()
    print (watch.get_number_of_watches_created())

    sEngrave = "Alfonso"
    if (watch.validateEngrave(sEngrave)):
        watch2 = watch.including_brand(sEngrave)
    print (watch.get_number_of_watches_created())

    sEngrave = 'foo@baz.com'
    if (watch.validateEngrave(sEngrave)):
        watch3 = watch.including_brand(sEngrave )
    print (watch.get_number_of_watches_created())
    
    sEngrave = "Alfonso" * 6
    if (watch.validateEngrave(sEngrave)):
        watch4 = watch.including_brand(sEngrave)
    print (watch.get_number_of_watches_created())

except  watchEngraveError as wError:
    print(wError, ':', wError.Engrave)