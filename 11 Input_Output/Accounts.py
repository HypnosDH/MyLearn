import hashlib

class AccountDB:
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    def __init__(self, name):
        self.name = name

    def encrypt(self ,string):
        return hashlib.sha256(string.encode()).hexdigest()

    def add(self, username, passwd):
        fout = open(self.name, "at", encoding="utf-8")
        encrypt_string = self.encrypt(passwd)
        print("{}:{}".format(username, encrypt_string), file=fout)
        fout.close()

    def Login(self, username, passwd):
        fin = open(self.name, "rt", encoding="utf-8")
        for line in fin:
            line = line.strip()
            oneLine = line.split(":")
            print(oneLine)
        fin.close()

    def Login2(self, username, passwd):
        fin = open(self.name, "rt", encoding="utf-8")
        lines = fin.readlines()
        fin.close()

        account_dict = {}
        for line in lines:
            line = line.strip()
            key, values = line.split(":")
            account_dict[key] = values
        
        return True if account_dict[username] == self.encrypt(passwd) else False


if __name__=="__main__":
    file = AccountDB("account.db")
    # file.add("Robert", "12345")
    # file.Login("Robert", "12345")
    if file.Login2("Robert", "12345"):
        print("Loin success!!")
    else:
        print("Loin Falid!!")