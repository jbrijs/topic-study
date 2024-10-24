from typing import List

'''
Leetcode #48 - Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''

def rotate(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """ 

        l,r = 0, len(matrix) - 1


        while l < r:
            for i in range(r - l):
                t, b = l, r

                top_left = matrix[t][l + i]

                #move bottom left to top left
                matrix[t][l + i] = matrix[b - i][l]

                # move bottom right to bottom left
                matrix[b - i][l] = matrix[b][r - i]

                # move top right to bottom right
                matrix[b][r - i] = matrix[t + i][r]

                # move top left to top right
                matrix[t + i][r] = top_left
            l += 1
            r -= 1