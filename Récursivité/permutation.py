class permutation:
    def __init__(self, blist):
        self.alist = blist
        self.permutation(len(self.alist))


    def swap(self, blist, i, j)
       blist[i], blist[j] = blist[j], blist[i]

    def permutation(self, taille):
        if taille == 1:
            print self.alist
        else:
            for i in range:
                self.swap(self.alist, i, taille-1)
                self.permutation(taille-1)
                self.swap(self.alist, i, taille-1)


