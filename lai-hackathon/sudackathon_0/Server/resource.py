import json
import pandas as pd

class TablesResource :
    def __init__ (self, df) :
        self.__tables = self.__initTables(df)
    
    def __initTables(self, df) :
        return [Table(row.table_id, row.seat_number) for idx, row in df.iterrows()]
    
    # dict形式で返す
    def getDict(self) :
        tables = [ table.getDict() for table in self.__tables ]
        obj = {
            "tables" : tables
        }
        return obj
    
    def on_get(self, req, resp) :
        resp.body = json.dumps(self.getDict(), ensure_ascii=False)

# =============================================================================
# テーブル一つのステートを管理するクラス
#  id : テーブルのid
#  seats : Seatクラスを持つ配列
# =============================================================================

class Table :
    def __init__ (self, id : str, seat_number) :
        self.__id = id
        self.__seats = self.__initSeats(seat_number)
    
    def __initSeats(self, seat_number) :
        return [ Seat(str(i), "init") for i in range(int(seat_number)) ]
    
    # dict形式で返す
    def getDict(self) :
        seats = [ seat.getDict() for seat in self.__seats ]
        obj = {
            "id" : self.__id,
            "seats" :  seats
        }
        return obj


# =============================================================================
#  座席一つのステートを管理するクラス
#  id : テーブル内のid
#  drink_state : 飲み物の状態
#     "init" -> 初期化
#     "nothing" ->　何も置いていない
#     "full" -> 満タン、もしくはそれに近い
#     "medium" -> そこそこ入っている
#     "empty" -> 空っぽ
# =============================================================================
        
class Seat :
    def __init__ (self, id : str, drink_state = "init") :
        self.__id = id
        self.__drink_state = drink_state
    
    # dict形式で返す
    def getDict(self) :
        obj = {
            "id" : self.__id,
            "drink_state" : self.__drink_state 
        }
        return obj
    
    def setDrinkState (self, drink_state) :
        self.__drink_state = drink_state
        