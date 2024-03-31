
prompts = [
    {
        "user_prompt": "In the given table A1:B14 find the mean, median and mode for both columns A and B FROM_SHEET data TO_SHEET data OUTPUT_LOCS A16, A17, A18, B16, B17, B18 ",
        "chat_gpt": "=AVERAGE(A1:A14);$;%=MEDIAN(A1:A14);$;%=MODE.SNGL(A1:A14);$;%=AVERAGE(B1:B14);$;%=MEDIAN(B1:B14);$;%=MODE.SNGL(B1:B14)"
    },

    {
        "user_prompt": "Generate a dummy dataset for market sales of pizza with attributes location, prices and quantity TO_SHEET data2 ",
        "chat_gpt": """
                    ={{"Location", "Prices", "Quantity"};
                    {"New York", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
                    {"Los Angeles", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
                    {"Chicago", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
                    {"Houston", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
                    {"Phoenix", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
                    {"Philadelphia", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
                    {"San Antonio", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
                    {"San Diego", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
                    {"Dallas", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
                    {"San Jose", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
                    {"Austin", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
                    {"Jacksonville", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)};
                    {"Fort Worth", RANDARRAY(10,1)*10, RANDBETWEEN(5,20)}}
                    """

    },
    {
        "user_prompt": " In the given table A1:B14 arrange the elements of the table in ascending order according to column A and rewrite the table FROM_SHEET data TO_SHEET data OUTPUT_LOCS D1 ",
        "chat_gpt": "=SORT(data!A1:B14, 1, TRUE)"
    },

    {
        "user_prompt": " In the given table A2:B14 compute the mean square error between the column A and B and label the column as `MSE` FROM_SHEET data TO_SHEET data OUTPUT_LOCS F2, F1 ",
        "chat_gpt": "=SUMSQ(data!A2:A14-data!B2:B14)/COUNTA(data!A2:A14);$;%MSE"
    },
    {
        "user_prompt": " Generate a dataset of 20 samples for jewellery inventory with SKU as the id. Other attributes are prices, quantity, feedback rating (out of 5), category (ENUMERATION -> 'necklace', 'ring', 'ear ring ' and 'payal') and link to images. TO_SHEET jewellery inventory OUTPUT_LOCS A1 ",
        "chat_gpt": """={"SKU","Prices","Quantity","Feedback Rating","Category","Image Link";
                    "SKU001",50,10,4.5,"necklace","https://example.com/image1.jpg";
                    "SKU002",30,15,4.2,"ring","https://example.com/image2.jpg";
                    "SKU003",40,8,4.7,"ear ring","https://example.com/image3.jpg";
                    "SKU004",60,12,4.8,"payal","https://example.com/image4.jpg";
                    "SKU005",55,11,4.3,"necklace","https://example.com/image5.jpg";
                    "SKU006",25,18,4.6,"ring","https://example.com/image6.jpg";
                    "SKU007",35,9,4.1,"ear ring","https://example.com/image7.jpg";
                    "SKU008",65,13,4.9,"payal","https://example.com/image8.jpg";
                    "SKU009",52,14,4.4,"necklace","https://example.com/image9.jpg";
                    "SKU010",28,17,4.5,"ring","https://example.com/image10.jpg";
                    "SKU011",38,7,4.8,"ear ring","https://example.com/image11.jpg";
                    "SKU012",70,11,4.2,"payal","https://example.com/image12.jpg";
                    "SKU013",48,16,4.6,"necklace","https://example.com/image13.jpg";
                    "SKU014",32,13,4.3,"ring","https://example.com/image14.jpg";
                    "SKU015",42,10,4.7,"ear ring","https://example.com/image15.jpg";
                    "SKU016",80,15,4.5,"payal","https://example.com/image16.jpg";
                    "SKU017",58,12,4.1,"necklace","https://example.com/image17.jpg";
                    "SKU018",36,19,4.4,"ring","https://example.com/image18.jpg";
                    "SKU019",46,8,4.9,"ear ring","https://example.com/image19.jpg";
                    "SKU020",90,14,4.2,"payal","https://example.com/image20.jpg"}
                """
    },

    {
        "user_prompt": """ In table A2:G21 consider "quantity" attribute. Filter out all the "SKU" from the table where quantity is less than 10 for all the samples in the table FROM_SHEET jewellery inventory TO_SHEET low inventory OUTPUT_LOCS A1 """,
        "chat_gpt": """=FILTER('jewellery inventory'!A2:G21, 'jewellery inventory'!C2:C21<10)"""
    },

    {
        "user_prompt": """ In table A2:G21 consider column C. Color all the rows red if quantity <10 , orange if quantity [10, 25) and green if quantity is >=25 FROM_SHEET jewellery inventory TO_SHEET jewellery inventory in OUTPUT_LOCS C1 """,
        "chat_gpt": """=IF(C2<10, "Red", IF(C2<25, "Orange", "Green"))"""
    },


]
