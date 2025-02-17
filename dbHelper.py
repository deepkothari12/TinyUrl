import mysql.connector as con


class dataBase:
    def __init__(self , long_url , alias) -> None:
        self.conn = con.connect(
            host="localhost",
            user = 'root',
            password = "2003",
            database = 'tiny'
        )
        print("Cooneeectionnn Doneeee")
        self.cursor = self.conn.cursor() #we have to make on cursor
        self.DBConnect() ##Call the DataBAse Connection Function 
        print("firstt Donee")
        self.InsertData(long_url = long_url , alias = alias)##Inserting Data
        print("Functionnn Calll Doneee")

    def DBConnect(self):
        try :
            self.cursor.execute(''' 
                                        CREATE TABLE IF NOT EXISTS tinyurl (
                                        id INT AUTO_INCREMENT,
                                        long_url TEXT,
                                        alias VARCHAR(255),
                                        PRIMARY KEY (id),
                                        UNIQUE(alias)
                                    
                                    );
                                ''')
            self.conn.commit()
            print("Donee")

        except Exception as e:
            print(e)

    
    def InsertData(self , long_url , alias):
        #print(long_url , alias)
        try:
            self.query = """ INSERT INTO tinyurl (long_url, alias) 
                             VALUES (%s, %s) """
            self.cursor.execute(self.query , (long_url , alias))
            self.conn.commit()
        except Exception as e:
            print("Error While Inserting Data" , e)



