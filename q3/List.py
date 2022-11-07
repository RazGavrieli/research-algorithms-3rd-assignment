class List(list):
    def __getitem__(self, keyTuple):
        """
        Enables accessing the list using a multi-dimensional syntax.
        >>> sampleList = List([[[1,2,3,33],[4,5,6,66]],[[7,8,9,99],[10,11,12,122]],[[13,14,15,155],[16,17,18,188]]])

        >>> sampleList[0,1,3] == 66
        True

        >>> sampleList[0] == [[1,2,3,33],[4,5,6,66]]
        True
        """
        if type(keyTuple) == int:
            return list(self)[keyTuple]
        res = list(self)
        for key in keyTuple:
            res = res[key]
        return res

    # def __setitem__(self, keyTuple, value):
    #     """
        
    #     """
    #     res = list(self)
    #     for key in keyTuple:
    #         res = res[key]
    #     res = value

if __name__ == "__main__":
    import doctest
    doctest.testmod()
