from rudiyov.dataset_structure import dataset


def insert_line(brands, price=None, quantities=None, skus=None, data=dataset):
    """
    insert one lines in brand
    :param brand: str, name of brand
    :param price: float,value of price
    :param quantities:dict
    :param skus:dict
    :param data:default dictionary
    :return: None
    """
    data[brands] = {
        'price.count': price,
        'quantities': quantities,
        'skus': skus
    }


def insert_dict(dictionary, data=dataset):
    """
    insert dictionary in database brand
    :param dictionary: dict
    :param data: dict, default dict
    :return: None
    """
    data.update(dictionary)


brand = "Adidas"
pricecount = 450.23
quant = {"dateSeen": ["2018-05-25T09:19:30.366Z", "2018-06-12T10:59:44.004Z"], "sourceURLs":
    "https://www.overstock.com/Clothing-Shoes/8858557/product.html",
         "value": 20}
skus_in = {"sourceURLs": "https://www.overstock.com/Clothing-Shoes/Liliana-Womens-EF63-Velvet-Pom-pom-Heels/14054533",
           "value": "312584628"}
insert_line(brand, pricecount, quant, skus_in)

# you can use both of method
dict = {
    'Adidas': {
        'prices.count': 450.23,
        'quantities': {"dateSeen": ["2018-05-25T09:19:30.366Z", "2018-06-12T10:59:44.004Z"], "sourceURLs":
            "https://www.overstock.com/Clothing-Shoes/8858557/product.html",
                       "value": 20},
        'skus': {
            "sourceURLs": "https://www.overstock.com/Clothing-Shoes/Liliana-Womens-EF63-Velvet-Pom-pom-Heels/14054533",
            "value": "312584628"}

    }
}
insert_dict(dict)
