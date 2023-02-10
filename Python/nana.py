scores = [12, 47, 30, 29, 19, 35]
high_scores= [score for score in scores if score > 20]
print(high_scores)
"""
To copy each score element in the new list, we write score as our expression, without applying any operation
"""

item_prices = [120, 25, 40]
under_50 = [price for price in item_prices if price < 50]
print(under_50)


websites = ["nytimes.com", "lemonde.fr", "economist.com"]
french = [website for website in websites if website.count(".fr") > 0]
print(french)


book_codes = ["FH2010", "BV1999", "LB2010"]
books_2010 = [code for code in book_codes if code.count("2010") == 1]
print(books_2010)