import pandas as pd


# 1 done
main_data = pd.read_csv('./input/main.csv')
main_data = main_data[main_data['COUNTRY'].str.contains("USA")]
main_data.to_csv('./output/filteredCountry.csv')


# 2 done
filtered_data = pd.read_csv('./output/filteredCountry.csv')
sku_output_df_sku = []
sku_output_df_First_minimum_price= []
sku_output_df_Second_minimum_price= []
uniq_skus = filtered_data['SKU'].unique()
for uniqsku in uniq_skus:  
    unique_sku_data = filtered_data[filtered_data['SKU'] == uniqsku]
    temp = unique_sku_data['PRICE'].str.strip('$')
    temp = temp.str.strip('?')
    temp  = temp.str.replace(',','').astype(float)
    nsmall = list(temp.nsmallest(2))
    if len(nsmall) > 1:
        sku_output_df_sku.append(list(unique_sku_data['SKU'])[0])
        sku_output_df_First_minimum_price.append(nsmall[0])
        sku_output_df_Second_minimum_price.append(nsmall[1])
    else:
        sku_output_df_sku.append(list(unique_sku_data['SKU'])[0])
        sku_output_df_First_minimum_price.append(nsmall[0])
        sku_output_df_Second_minimum_price.append(nsmall[0])

sku_output_df = pd.DataFrame(
    {'SKU': sku_output_df_sku,
     'First_minimum_price': sku_output_df_First_minimum_price,
     'Second_minimum_price': sku_output_df_Second_minimum_price
    })
sku_output_df.to_csv('./output/lowestPrice.csv')