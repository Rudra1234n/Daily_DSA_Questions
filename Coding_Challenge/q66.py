def sumdig(self, y):

        if y == 0:

            return 0

        else: 

            q = y % 10

            return q * q + self.sumdig(y // 10)

    

    def ishappy(self, z):

        sumd = self.sumdig(z)  

        if sumd > 9:

            return self.ishappy(sumd)  

        else:

            if sumd == 1:

                return True

            else: 

                return False

    

    def nextHappy(self, n):

        x = n + 1

        z = False

        while z is not True:

            z = self.ishappy(x)  

            if not z:

                x += 1

        return x
