import mysql.connector as con


class dataBase:
    def __init__(self) -> None:# , long_url , alias) -> None:
        self.conn = con.connect(
            host="localhost",
            user = 'root',
            password = "2003",
            database = 'tiny'
        )
       # print("Cooneeectionnn Doneeee")
        self.cursor = self.conn.cursor() #we have to make on cursor
       # self.DBConnect() ##Call the DataBAse Connection Function 
       # print("firstt Donee")
       # self.InsertData(long_url = long_url , alias = alias)##Inserting Data
       # print("Functionnn Calll Doneee")

    def DBConnect(self, long_url , aliass):
        try :
            #print(aliass)
            self.cursor.execute(''' 
                                
                                    CREATE TABLE IF NOT EXISTS tinyurl (
                                    id INT AUTO_INCREMENT,
                                    long_url TEXT,
                                    aliass VARCHAR(255),
                                    PRIMARY KEY (id),
                                    UNIQUE(aliass)
                                    );
                                
                                ''')
            #print(aliass)
            self.conn.commit()
            self.InsertData(long_url , aliass)
          #  print("Donee")

        except Exception as e:
            print(e)

    
    def InsertData(self , long_url , aliass):
        #print(long_url , alias)
        try:
            self.query = """ INSERT INTO tinyurl (long_url, aliass) 
                             VALUES (%s, %s) """
            self.cursor.execute(self.query , (long_url , aliass))
            self.conn.commit()
        except Exception as e:
            print("Error While Inserting Data" , e)



    def FindData(self  , aliass):
        try:
            print("aliass" , aliass)
            self.querys ="""
                        
                        SELECT long_url FROM tinyurl WHERE aliass = %s
                        
                        """
            self.cursor.execute(self.querys , (aliass,))##arguent shoud be tupple that why ","
            print("Executeeee -->>")
            ans = self.cursor.fetchone() ##return the tupple
            #print(ans)
            # self.conn.commit() no need bcz select not modify databse 
            if ans:
                s = []
                for i in ans:
                    s.append(i)
                return s[0]
            
        except Exception as e:
            print("Not Found")


        # def aliasSearch(self , aliass):
        #     try:
        #         self.querys ="""
        #                 SELECT long_url FROM tinyurl WHERE 
        #             """
        #     except:
        #         pass
        


