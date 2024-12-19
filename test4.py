# class Zergling:
#     def __init__(self):
#         self.hp = 20
#         self.mana = 50
    
#     def run(self): #메서드
#         print("뛴다")
#         self.hp -= 1
#         self.mana += 1

#     def show_state(self):
#         print(f'HP : {self.hp}')
#         print(f'mana : {self.mana}')

# z1 = Zergling() #인스턴스
# z2 = Zergling()
# z1.run()
# z1.show_state()
# z2.run()
# z2.run()
# z2.run()
# z2.run()
# z2.run()
# z2.show_state()

# class GameMachine:
#     def __init__(self):
#         self.coin = 0
    
#     def input_coin(self, coin):
#         if 0< coin <= 5 and (self.coin + coin) <= 10: 
#             self.coin += coin
#         else:
#             return
    
#     def play_game(self):
#         if self.coin > 0 :
#             self.coin -= 1
#             print("게임 재밌다")
#         else:
#             print("코인을 넣어주세요")

    
#     def show_status(self):
#         print(f'남아있는 코인은 {self.coin}입니다')

# gm = GameMachine()
# gm.input_coin(2)
# gm.show_status()
# gm.play_game()
# gm.show_status()

# class super:
#     def run(self) : print("런")

# class son1(super):
#     def ran(self) : print("랜")

# class son2(super):
#     def run(self) : print("런런")
#     def ron(self) : print("론")

# tire1 = son1()
# tire1.run()
# tire1.ran()

import numpy as np

lst = [1,2,3,4,5]
result_lst = lst*2
print(result_lst)
numpy_array = np.array([1,2,3,4,5])
result_array = numpy_array * 2
print(result_array)