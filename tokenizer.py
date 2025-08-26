import re
class Tokenizer():
    def __init__(self):        
        with open('shake_spear.txt','r',encoding='utf-8') as file:
            self.data=file.read()

    def character_tokenizer(self):
        'converts the characters to int and stores the dataset'
        chars=sorted(set(self.data))
        self.string_to_int = { ch:i for i,ch in enumerate(chars) }
        self.int_to_string = { i:ch for i,ch in enumerate(chars) }

    def word_tokenizer(self):
        'converts the words to int and stores the dataset'
        text = self.data.lower()
        words = re.findall(r"\w+|[^\w\s]", text, re.UNICODE)
        tokens = [i.removeprefix('_') for i in words]
        chars = sorted(set(tokens))
        self.string_to_int = { ch:i for i,ch in enumerate(chars) }
        self.int_to_string = { i:ch for i,ch in enumerate(chars) }

    def encoder(self,s:str)->int:
        'converts str to int'
        return [self.string_to_int[ch] for ch in s]
    
    def decoder(self,l:int)->str:
         'converts int to str'
         return ''.join([self.int_to_string[i]+" " for i in l])
    
if __name__=='__main__':
    obj=Tokenizer()
    # obj.character_tokenizer()
    # print(obj.encoder(s='gokul'))
    obj.word_tokenizer()
    # print(obj.encoder(s=["to","be","or","not","to","be"]))
    print(obj.decoder([22487, 2135, 15357, 15016, 22487, 2135]))