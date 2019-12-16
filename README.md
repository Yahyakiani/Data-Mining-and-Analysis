Note: This Project is compatible for both Windows and Linux.


-First of all create a python virtual enviroment
Linux:
--virtualenv enviroment
Windows:
-- python -m venv enviroment

-Then activate it by the following command
Linux:
-- source venv/bin/activate
Windows:
-- Scripts/activate
-After that install all the requirements in the virtual enviroment by the following command
-- pip install -r requirements.txt

-When all of the above procedure is complete, run the program from the following the command in main directory
Linux:
--python3 run.py
Windows:
--python run.py

There 2 options avaialble to execute the code.

Option 1:

It will start extracting data using arbitrary browser agent constraints from the given website and start dumping the data in a csv file.The
request delay for each page is 4 seconds to bypass request blockage.

Option 2:
It will start performing data analysis on the gathered data.Analysis is done using pandas library.This is the information
on which it performs analysis.

Views:
![alt text](./views/analysis.jpg)

Analysis Part:


adidas
Max Price:299.0 € [Product Name:adidas Performance Alphaedge 4D - Star Wars,Product Url:https://www.snkrs.com/en/adidas-performance/adidas-performance-alphaedge-4d-star-wars-10390.html]


Min Price:53.4 € [Product Name:adidas Tyshawn - Core Black/White,Product Url:https://www.snkrs.com/en/adidas/adidas-tyshawn-core-blackwhite-9963.html]


Average Brand Price:116.62682926829277






Stussy
Max Price:199.0 € [Product Name:Stussy Mix Up Cord Jacket - Brown,Product Url:https://www.snkrs.com/en/stussy/stussy-mix-up-cord-jacket-brown-10425.html]


Min Price:49.0 € [Product Name:Stussy Big Logo Plaid Low Pro Cap - Black,Product Url:https://www.snkrs.com/en/stussy/stussy-big-logo-plaid-low-pro-cap-black-10430.html]


Average Brand Price:107.44444444444444






Reebok
Max Price:299.0 € [Product Name:Reebok Daytona DMX MISBHV - Black/Solar Green,Product Url:https://www.snkrs.com/en/reebok/reebok-daytona-dmx-misbhv-blacksolar-green-9744.html]


Min Price:28.0 € [Product Name:Reebok Classics Vector Bucket Hat - Black,Product Url:https://www.snkrs.com/en/reebok/reebok-classics-vector-bucket-hat-black-10475.html]


Average Brand Price:122.2470588235294






Converse
Max Price:139.0 € [Product Name:Converse Chuck Taylor MC18 High - Carbon Grey,Product Url:https://www.snkrs.com/en/converse/converse-chuck-taylor-mc18-high-carbon-grey-10408.html]


Min Price:59.5 € [Product Name:Converse Chuck Taylor All Star 70 OX - Renew Denim,Product Url:https://www.snkrs.com/en/converse/converse-chuck-taylor-all-star-70-ox-renew-denim-9410.html]


Average Brand Price:95.74285714285713






Nike
Max Price:475.0 € [Product Name:Nike Gore-Tex M65 Jacket - Dark Grey,Product Url:https://www.snkrs.com/en/nike/nike-gore-tex-m65-jacket-dark-grey-10407.html]      


Min Price:41.3 € [Product Name:Nike ACG LS GX Waffle Top - Habanero Red,Product Url:https://www.snkrs.com/en/nike/nike-acg-ls-gx-waffle-top-habanero-red-10285.html]


Average Brand Price:121.03486238532085






Nike
Max Price:475.0 € [Product Name:Nike Gore-Tex M65 Jacket - Black,Product Url:https://www.snkrs.com/en/nike/nike-gore-tex-m65-jacket-black-10406.html]


Min Price:41.3 € [Product Name:Nike ACG LS GX Waffle Top - Habanero Red,Product Url:https://www.snkrs.com/en/nike/nike-acg-ls-gx-waffle-top-habanero-red-10285.html]


Average Brand Price:121.03486238532085






Puma
Max Price:159.0 € [Product Name:Puma Cell Alien Ader Error - White,Product Url:https://www.snkrs.com/en/puma/puma-cell-alien-ader-error-white-10338.html]


Min Price:79.0 € [Product Name:Puma Fast Rider OG - Black,Product Url:https://www.snkrs.com/en/puma/puma-fast-rider-og-black-10320.html]


Average Brand Price:100.7111111111111






Vans
Max Price:109.0 € [Product Name:Vans OG Sk8-Hi LX - Stargazer/Blue Mirage,Product Url:https://www.snkrs.com/en/vans/vans-og-sk8-hi-lx-stargazerblue-mirage-10392.html]


Min Price:59.5 € [Product Name:Vans OG Old Skool LX - Castlerock/Pearl Gray,Product Url:https://www.snkrs.com/en/vans/vans-og-old-skool-lx-castlerockpearl-gray-10016.html]


Average Brand Price:74.11538461538461






New
Max Price:169.0 € [Product Name:New Balance M577 TGK - Made in UK,Product Url:https://www.snkrs.com/en/new-balance/new-balance-m577-tgk-made-in-uk-10382.html]     


Min Price:66.5 € [Product Name:New Balance CM997 HDL - White/Navy,Product Url:https://www.snkrs.com/en/new-balance/new-balance-cm997-hdl-whitenavy-9965.html]      


Average Brand Price:106.5090909090909






adidas
Max Price:299.0 € [Product Name:adidas ZX 4000 4D I Want I Can - Black/Hi-Res Yellow,Product Url:https://www.snkrs.com/en/adidas/adidas-zx-4000-4d-i-want-i-can-blackhi-res-yellow-10345.html]


Min Price:53.4 € [Product Name:adidas Tyshawn - Core Black/White,Product Url:https://www.snkrs.com/en/adidas/adidas-tyshawn-core-blackwhite-9963.html]


Average Brand Price:116.62682926829277






Asics
Max Price:195.0 € [Product Name:Asics Gel Kayano 5 360 Gore-Tex - Oatmeal/Lichen Roc,Product Url:https://www.snkrs.com/en/asics/asics-gel-kayano-5-360-gore-tex-oatmeallichen-roc-10222.html]


Min Price:56.0 € [Product Name:Asics Gel Venture 7 - Black/Tan Presidio,Product Url:https://www.snkrs.com/en/asics/asics-gel-venture-7-blacktan-presidio-10155.html]


Average Brand Price:112.845






Asics
Max Price:195.0 € [Product Name:Asics Gel Kayano 5 360 Gore-Tex - Cool Mist,Product Url:https://www.snkrs.com/en/asics/asics-gel-kayano-5-360-gore-tex-cool-mist-10223.html]


Min Price:56.0 € [Product Name:Asics Gel Venture 7 - Black/Tan Presidio,Product Url:https://www.snkrs.com/en/asics/asics-gel-venture-7-blacktan-presidio-10155.html]


Average Brand Price:112.845






Jordan
Max Price:384.3 € [Product Name:Jordan PSG Varsity Jacket - Black/White,Product Url:https://www.snkrs.com/en/jordan/jordan-psg-varsity-jacket-blackwhite-10314.html]


Min Price:20.3 € [Product Name:Jordan PSG Beanie - Black,Product Url:https://www.snkrs.com/en/jordan/jordan-psg-beanie-black-10368.html]


Average Brand Price:116.47619047619048






Carhartt
Max Price:139.3 € [Product Name:Carhartt WIP Jones Pullover - Camo Tree Orange,Product Url:https://www.snkrs.com/en/carhartt-wip/carhartt-wip-jones-pullover-camo-tree-orange-10301.html]


Min Price:90.3 € [Product Name:Carhartt WIP Whitsome Shirt Jac - Dark Navy,Product Url:https://www.snkrs.com/en/carhartt-wip/carhartt-wip-whitsome-shirt-jac-dark-navy-10302.html]


Average Brand Price:114.80000000000001



Products that are on sale and their total count



Brand
Asics       13
Carhartt     2
Converse    12
Jordan      11
New         20
Nike        77
Puma         6
Reebok       4
Vans         9
adidas      22
Name: Name, dtype: int64
