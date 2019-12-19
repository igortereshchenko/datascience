from dataset_structure import dataset
new_flight={
    7777777:{
        "neighbourhood":"Meninghton",
        "state":"WA",
        "market":"Seattle",
        "country":"United States"
    }
}
dataset.update(new_flight)
print(dataset)