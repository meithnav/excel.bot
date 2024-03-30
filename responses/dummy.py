
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
    }

]
