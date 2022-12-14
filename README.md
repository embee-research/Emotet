# Emotet_Hashing.py

A script to perform lookups of API hashes utilised by recent (2022-November) Emotet Samples. 

Written by @embee_research @Huntresslabs
- https://twitter.com/embee_research
- https://www.huntress.com/

## Usage


`emotet_hashing.py <hash_value>` 

(Make sure to place the relevant dll's in the same folder as the script so that they can be parsed correctly, or place the script in the c:\\windows\\system32\\ folder)


<img width="614" alt="image" src="https://user-images.githubusercontent.com/82847168/199856599-cd6b3c3c-607d-42dd-b468-b96420a27d0f.png">



<img width="990" alt="image" src="https://user-images.githubusercontent.com/82847168/199859979-ea07346d-c25c-49d1-90d1-efac694c4465.png">



## Samples 
- https://bazaar.abuse.ch/sample/2b3055acdff4d4f808f6e87211fe620ad11bf0508404d5b3364e98b82ec240cb/
- https://bazaar.abuse.ch/sample/cbd6adc88d18378d5e2e68cae7cdd1125359a4085a9070407779e1f3344e91c9/

## Notes
- The above links are to packed emotet samples, you will need to unpack them first. (VirtualAlloc + Hardware Breakpoint will work)
- The Emotet samples have a key that is used to encode the API hashes, this changes between samples and you may need to update it. 
- To find the key, locate the function that hashes the api name, and note the key after the return. 

<img width="554" alt="image" src="https://user-images.githubusercontent.com/82847168/199857070-8372737a-d143-4e9f-9241-7217b6412a99.png">


<img width="896" alt="image" src="https://user-images.githubusercontent.com/82847168/199856898-5981c6b2-5696-4dc1-9b33-2ab18dc34954.png">

<img width="823" alt="image" src="https://user-images.githubusercontent.com/82847168/199857007-ed85996a-cbd5-4e45-bb13-1996bae3fa76.png">


## Examples 

<img width="690" alt="image" src="https://user-images.githubusercontent.com/82847168/199857222-38a149de-5682-4001-bc16-d03615760525.png">





