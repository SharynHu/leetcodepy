class TreeAncestor(object):

    def __init__(self, n, parent):
        """
        :type n: int
        :type parent: List[int]
        """
        parent = dict(enumerate(parent))
        # store all 1-th ancesstor for each node
        ancesstor = [parent]
        # this jump part is a little bit tricky. 
        #  for the first time, for each i, you will get parent[parent[i]] that is the 2-th ancesstor of i. 
        # for the second time, for each i, parent[i] already gives us the 2-th accesstor, so parent[parent[i]] will give us the 4-th ancesstor.
        # ...
        
        for s in xrange(int(log(len(parent))+1)):
            upper = {}
            for i in parent:
                if parent[i] in parent:
                    upper[i] = parent[parent[i]]
            ancesstor.append(upper)
            parent = upper
        self.ancesstor = ancesstor
        print(ancesstor)

    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        step = int(log(k)+1)
        while k > 0 and node > -1:
            if k >= 1 << step:
                node = self.ancesstor[step].get(node, -1)
                k -= 1 << step
            else:
                step -= 1
        return node
