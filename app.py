from global_news import main_page

news ={
    "global_news":{
        "eu":[],
        "us":[],
        "tech":[],
        "ent":[],
        "other":[]
    }
}


main_page(news["global_news"]["eu"],
      news["global_news"]["us"],
      news["global_news"]["tech"],
      news["global_news"]["ent"],
      news["global_news"]["other"])



print(news["global_news"]["other"])
