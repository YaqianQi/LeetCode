"""
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array sweetness.

You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1 pieces using K cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.
"""

if __name__ == "__main__":
    Input: sweetness = [1,2,3,4,5,6,7,8,9] 
    K = 5
    # Output: 6
    # Explanation: You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]


    Input: sweetness = [5,6,7,8,9,1,2,3,4]
    K = 8
    # Output: 1
    # Explanation: There is only one way to cut the bar into 9 pieces.


    #Input: 
    sweetness = [1,2,2,1,2,2,1,2,2] 
    K = 2
    #Output: 5
    #Explanation: You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]