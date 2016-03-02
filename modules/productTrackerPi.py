import sys
sys.path.append('/home/pi/Repos/Personal-Assistant/modules/productSites')

# NEED TO MAKE THIS DYNAMIC (add to file a list of websites)
websites = ["amazon", "google", "nike", "Papa John"]

def queryProduct(productName):
    # Some code goes here that queries the string input: 
    #   - categorizes the product
    #   - decides which website to use
    #   - searches website for information
    #   - asks for clarification
    #   - saves information on a database:
    #          - prices, lowest price, product name, if sale, etc.
    print "hi"

    
queryProduct('Sperry Topsiders')