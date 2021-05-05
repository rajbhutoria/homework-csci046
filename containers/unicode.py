import unicodedata


class NormalizedStr:
    '''
    By default, Python's str type stores any valid unicode string.
    This can result in unintuitive behavior.
    For example:

    >>> 'César' in 'César Chávez'
    True
    >>> 'César' in 'César Chávez'
    False

    '''

    def __init__(self, text, normal_form='NFC'):
        self.text = text
        self.normal_form = normal_form

    def __repr__(self):
        '''
        '''
        h1 = unicodedata.normalize(self.normal_form, self.text)
        return "NormalizedStr('" + h1 + "', '" + self.normal_form + "')"

    def __str__(self):
        '''
        This functions converts the NormalizedStr into a regular string object.
        '''
        return unicodedata.normalize(self.normal_form, self.text)

    def __len__(self):
        '''
        Returns the length of the string.
        '''
        return len(unicodedata.normalize(self.normal_form, self.text))

    def __contains__(self, substr):
        '''
        Returns true if the `substr` variable is contained within `self`.
        '''
        self.substr = substr
        return unicodedata.normalize(self.normal_form, substr) in \
            unicodedata.normalize(self.normal_form, self.text)

    def __getitem__(self, index):
        '''
        Returns the character at position `index`.
        '''
        self.index = index
        return unicodedata.normalize(self.normal_form, self.text)[index]

    def lower(self):
        '''
        Returns a copy in the same normalized form, but lower case.
        '''
        return unicodedata.normalize(self.normal_form, self.text).lower()

    def upper(self):
        '''
        Returns a copy in the same normalized form, but upper case.
        '''
        return unicodedata.normalize(self.normal_form, self.text).upper()

    def __add__(self, b):
        '''
        Returns a copy of `self` with `b` appended to the end.
        '''
        norm_self = unicodedata.normalize(self.normal_form, str(self.text))
        norm_b = unicodedata.normalize(self.normal_form, str(b))
        unfiltered_combo = norm_self + norm_b
        norm_combo = unicodedata.normalize(self.normal_form, unfiltered_combo)
        return NormalizedStr(norm_combo)

    def __iter__(self):
        '''
        '''
        return NormalizedStrIter(self.__str__())


class NormalizedStrIter:

    def __init__(self, text, n=-1):
        self.text = text
        self.n = n

    def __next__(self):
        if self.n == (len(self.text) - 1):
            raise StopIteration
        else:
            self.n += 1
            return self.text[self.n]
