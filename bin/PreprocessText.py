import re

class PreprocessText:
    """"
    preprocess articles read from file
    """

    def __init__(self):
        pass

    def convertToLower(self,text):
        """"
        converts text to lowercase
        Input:
            text:String
        Output:
            text:String
        """

        loweredText=text.lower()
        return loweredText

    def removeSpecialChar(self,text):
        """
        removes special characters from text
        """
        processedText=re.sub(',|;|<|>',text,'')
        return processedText

# if __name__=="__main__":
#     preprocessObj=PreprocessText()
#     text="Hi Hello The Prime Minister gave a speech today"
#     loweredText=preprocessObj.convertToLower(text)
#     filteredText=preprocessObj.removeSpecialChar(text)
#     print("loweredText is :",loweredText)
#     print("filteredText is : ",filteredText)
