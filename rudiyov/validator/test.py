from rudiyov.validator.lib import *

if brand_validator("Tommy Hilfiger"):
    print("Brand is correct")
else:
    print("Brand is incorrect")
# the answer must be "Brand is correct"
if quantities_validator({"dateSeen": ["2017-03-25T09:19:30.366Z", "2017-02-12T10:59:33.004Z"], "sourceURLs":
    "https://www.overstock.com/Clothing-Shoes/Womens-Propet-Tour-Walker-Hook-Loop-Sport-White/8858557/product.html",
                         "value": 19}):
    print("quantities is correct")
else:
    print("quantities is incorrect")
# the answer must be "quantities is correct"
if skus_validator({"sourceURLs":
                       "https://www.overstock.com/Clothing-Shoes/Liliana-Womens-EF63-Velvet-Pom-pom-Heels/14054533/product.html",
                   "value": "20669369"}):
    print("skus is correct")
else:
    print("skus is incorrect")
# the answer must be "skus is correct"
if pricecount_validator("200.124"):
    print("price.count is correct")
else:
    print("price.count is incorrect")
# the answer must be "price.count is correct"
