# ###########################################################
# how to generate probability table (or dictionary)
# làm phép thử thôi (trading, thống kê hoặc làm khỉ gì đó)
# get candle data
# plotting
# pattern recognition
# ###########################################################
# on tap toan
import numpy as np


# reference:
# --------------------------------------------------------------------------------------------------------------

# # ------------------- example 1--------------
# a = array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
#            ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
#            ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
#            ['Sun', 13, 15, 19, 16]])

# print(a)
# print()

# m = reshape(a, (7, 5))
# print(m)
# # # for item in m[2]:
# # for item in m:
# #     print(item)
# #     # print(type(item))
# # # print(m[2])

# ------------------- example 2--------------
# tmp = [1, 2, 3], [[4, 5, 6], [7, 8, 9]]
# --------------------
# thanh 1 the thong nhat luon
# tmp = np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])

# --------------------

# tmp = np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis=0)
# tmp = [[1, 2, 3], [4, 5, 6]], [7, 8, 9]
# tmp = np.append([[1, 2, 3], [4, 5, 6]], [7, 8, 9], axis=0)

# print(tmp)
# for i in tmp:
#     print(i)

# ------------------- example 3--------------
# a = np.array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
#               ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
#               ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
#               ['Sun', 13, 15, 19, 16]])
# # Adding a row
# m = np.reshape(a, (7, 5))
# m = np.append(m, [['Avg', 12, 15, 13, 11]], 0)

# Adding a columns
# m = np.insert(m, [5], [[1], [2], [3], [4], [5], [6], [7]], 1)

# Delete a row
# m = np.delete(m, [3], 0)

# Delete a columns
# m = np.delete(m, [3], 1)

# Update a row
# m[2] = ['Wed', 11, 20, 22, 19]

# Update a column
# m[:, 1] = [12, 15, 13, 11, 12, 15, 13]

# print(m)

# ------ reshape/ append/ insert/ delete/ m[2]/ m[:, 1] ------

# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------
# multivariate normal distribution

# 2 dimensional normal distribution python
# https://www.google.com/search?q=2+dimensional+normal+distribution+python&sxsrf=ALeKk01xBnhfRRU-iF3SeahUb-Otgv1iFQ%3A1621258191814&ei=z2-iYPmfMYTLmAWV4JNY&oq=2+dimensional+normal+distribution+python&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoHCAAQRxCwAzoCCABQtyhYzDJggDRoAXACeACAAdEBiAHSCZIBBTAuNS4ymAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=gws-wiz&ved=0ahUKEwi5w_K06dDwAhWEJaYKHRXwBAsQ4dUDCA4&uact=5

# random variable function python
# https://www.google.com/search?q=random+variable+function+python&sxsrf=ALeKk01FFpc534tDHZwBRCCoaJ_wTiZfYQ%3A1621258282326&ei=KnCiYIuzE7SYr7wPlYW-qA4&oq=random+variable+function+python&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEBYQHjoHCAAQRxCwAzoHCAAQsAMQQzoCCABQ7SJY3jJg4jNoAXACeACAAdUBiAG2CZIBBTAuNi4xmAEAoAEBqgEHZ3dzLXdpesgBCsABAQ&sclient=gws-wiz&ved=0ahUKEwiL8Ibg6dDwAhU0zIsBHZWCD-UQ4dUDCA4&uact=5

# simpson distribution python
# https://www.google.com/search?q=simpson+distribution+python&bih=915&biw=960&hl=en&sxsrf=ALeKk03mTjPHRYbUxRYSNc0LQQIpygf0Xw%3A1621258524284&ei=HHGiYJLbEKCSr7wPhaexqAk&oq=simpson+distribution+python&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BggAEBYQHjoHCCEQChCgAToECCEQFVCBGVjdJmCiKGgBcAJ4AIAB3gGIAfgKkgEFMC42LjKYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=gws-wiz&ved=0ahUKEwiS2bbT6tDwAhUgyYsBHYVTDJUQ4dUDCA4&uact=5

# convergence random variables python
# https://www.google.com/search?q=convergence+random+variables+python&bih=915&biw=960&hl=en&sxsrf=ALeKk01nu9gWauqKde0QAzDRapHrT0RYsg%3A1621258530563&ei=InGiYL7dIb-Tr7wP1-isiA0&oq=convergence+random+variables+python&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BAgjECc6BQgAEJECOggIABCxAxCDAToICC4QxwEQowI6BAguEEM6BAgAEEM6AggAOgsILhCxAxDHARCjAjoFCAAQsQM6CwguEMcBEKMCEMsBOgUIABDLAToGCAAQFhAeOgUIIRCgAToHCCEQChCgAVDJvwNYt78EYJPBBGgBcAJ4AYABmgKIAfcbkgEGMC4yMS4ymAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient=gws-wiz&ved=0ahUKEwi-9rXW6tDwAhW_yYsBHVc0C9EQ4dUDCA4&uact=5

# laplace distribution python
# https://www.google.com/search?q=laplace+distribution+python&oq=laplace+distribution+pyth&aqs=chrome.0.0j69i57j0i22i30l3.6182j0j9&sourceid=chrome&ie=UTF-8

# central limit theorem python
# https://www.google.com/search?q=central+limit+theorem+python&sxsrf=ALeKk03OHGaZtuue9vWL9EwPk2qLClx0jw%3A1621258727162&ei=53GiYPamCY-K0wSolYz4DQ&oq=central+limit+theorem+python&gs_lcp=Cgdnd3Mtd2l6EAMyAggAMgIIADIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BwgAELADEEM6BAgAEEM6BQgAEMsBOgcIABCHAhAUUNoGWMsPYIoRaAFwAngAgAGSAYgBgQiSAQMwLjiYAQCgAQGqAQdnd3Mtd2l6yAEKwAEB&sclient=gws-wiz&ved=0ahUKEwi2tpW069DwAhUPxZQKHagKA98Q4dUDCA4&uact=5

# law of large numbers python
# https://www.google.com/search?q=law+of+large+numbers+python&oq=Law+of+large+numbers+python&aqs=chrome.0.0j0i22i30.1708j0j4&sourceid=chrome&ie=UTF-8

# Convergence in probability python
# https://www.google.com/search?q=Convergence+in+probability+python&oq=Convergence+in+probability+python&aqs=chrome..69i57j0i22i30.1693j0j4&sourceid=chrome&ie=UTF-8

# frequency table statistics python
# https://www.google.com/search?q=frequency+table+statistics+python&sxsrf=ALeKk03ERCTI53zIXYFfKcSn4xS7_8WqYg%3A1621259295763&ei=H3SiYLPuLcrEmAWm7qrwAg&oq=frequency+table+statistics+python&gs_lcp=Cgdnd3Mtd2l6EAMyCAghEBYQHRAeMggIIRAWEB0QHjIICCEQFhAdEB4yCAghEBYQHRAeMggIIRAWEB0QHjIICCEQFhAdEB4yCAghEBYQHRAeOgoIABCxAxCDARBDOgQILhBDOgUIABDLAToCCAA6BQgAEJECOgcIABCHAhAUOgYIABAWEB5QrjNY93pgxHxoAHACeACAAYECiAHRF5IBBjAuMjAuMZgBAKABAqABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz&ved=0ahUKEwjz-aXD7dDwAhVKIqYKHSa3Ci4Q4dUDCA4&uact=5

# taylor equation
# https://stackoverflow.com/questions/59380645/taylor-expansion-in-python

# pandas correlation
# https://stackoverflow.com/questions/42579908/use-corr-to-get-the-correlation-between-two-columns


import tradingeconomics
# get data from:
# https://www.forexfactory.com/
# https://www.forexlive.com/
# https://www.fxstreet.com/news/feed
