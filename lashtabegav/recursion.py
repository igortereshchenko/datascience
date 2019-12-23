example = {
    
	"956883": {

        "number_of_reviews": 207,

        "review_scores_value": 30,

        "country": "United States"

    },

    "5177328": {

        "number_of_reviews": 43,

        "review_scores_value": 10,

        "country": "United States"

    },
    "16708587": {

        "number_of_reviews": 9,

        "review_scores_value": 5,

        "country": "United States"

    }

}


def iterate(d, hid):

    for k, v in d.items():

        if isinstance(v, dict):

            iterate(v, k)

        else:

            if hid is not 0:

                obj = example[hid]

                if obj['number_of_reviews'] > 10 and obj['review_scores_value'] > 10:

                    print(obj)


iterate(example, 0)


