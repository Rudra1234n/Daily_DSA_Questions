class Solution:
    steps = 0
    def toh(self, N, source, destination, auxiliary):
        # Your code here
        if N == 1:
            print("move disk {} from rod {} to rod {}".format(N, source, destination))
            return self.steps + 1
        self.steps=self.toh(N-1,source,auxiliary,destination)
        print("move disk {} from rod {} to rod {}".format(N, source, destination))
        self.steps += 1
        self.steps=self.toh(N-1,auxiliary,destination,source)
        return self.steps
