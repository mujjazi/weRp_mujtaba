**weRp_mujtaba**

**Author: Mujtaba Mehdi**

## Website Automation with Selenium and Python

*Note: 
This project is currently working on Macbook Pro running on macOS Mojave 10.14 Beta using Python 2.7 and Selenium 3.13 64 bit*

*This project is also working on Toshiba Satellite P750 running on Windows 7 64 bit using Python 2.7 and Selenium 3.13 64 bit.*

## Installation and Downloads:

Please follow the instructions mentioned in the below link based on your operating system.

**Selenium**: https://selenium-python.readthedocs.io/installation.html


*Note: Chrome, Firefox and Internet Explorer driver files have been included in the project and for different Opearating systems other than Windows, PLease download using the link provided below.*

**Chrome Driver**: https://chromedriver.storage.googleapis.com/index.html?path=2.41/

**Firefox Gecko Driver**: https://github.com/mozilla/geckodriver/releases

**IEWebDriver**: http://selenium-release.storage.googleapis.com/index.html?path=3.13/

**Safari**: https://selenium-python.readthedocs.io/installation.html

**Edge**: https://selenium-python.readthedocs.io/installation.html


**Note: The folders Test1 and Test2 contain all the files relevant to Case 1 and Case 2 respectively**


## Case 1: Front-end Automation

**Web site's URL is** -> https://www.nisnass.ae/

# 1.1 Register Account

We need you to register an account on nisnass through automation

Verify that after logging into the account the “Email-Address” field is un-editable

Verify it is the same email with which you registered the account

Update the phone number to “+97167324238” and verify it is updated

Please make edge case scenarios in this and verify them in the test-cases

# 1.2 Add to Bag

Write a test-case which can add these types of items into the bag and then verify that they are added into the “Bag”:

https://www.nisnass.ae/shop-quench-intense-hydration-mask-1-sheet-for-womens-212054000.html

One Size item into the bag

https://www.nisnass.ae/shop-zitah-classic-pumps-for-womens-212061761.html

Pink Color with 9.5 sized item into the bag

https://www.nisnass.ae/shop-metallic-sandals-for-womens-212224468.html

Size 40 into the bag 

*If these items are not available on website, please chose any other item with one size, different color and different size item.* 

 
 
## Case 2: Front-end Automation

**Web site URL is** - > https://www.ounass.ae/

## 2.1 Login through Facebook


Click on to User icon in top left

Click Amber button

Click Facebook connect (Use any test Facebook account)

Get your user authenticated

Come back to website and verify user is successfully logged in

## 2.2 Product Listing Page

Verify when you go to product listing page i.e. Clothing etc. -> https://www.ounass.ae/clothing/

After 72 items, “View More” should not automatically load more, but need to be clicked button at bottom which should load more items if there are more than 12 items in this page.

After selecting “Christian Siriano” from filters only 2 results are found

Verify products only with title “Christian Sirano” as a brand is displayed

